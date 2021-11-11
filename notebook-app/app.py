from kubernetes import config, dynamic
from kubernetes.client import api_client
from kubernetes.client.api import core_v1_api
from flask import Flask, request, jsonify, render_template, make_response
from hashlib import blake2b
import configparser
import sqlite3
import datetime

app = Flask(__name__)

properties = configparser.ConfigParser()
properties.read('hashes.ini')
secret_key = bytes(properties.get('Hashes', 'SECRET_KEY'), encoding='utf-8')
digest_size = int(properties.get('Hashes', 'DIGEST_SIZE'))

config.load_kube_config()
api = core_v1_api.CoreV1Api()

def create_pod():
    config.load_kube_config()
    api = core_v1_api.CoreV1Api()
    pod_manifest = {
        'apiVersion': 'v1',
        'kind': 'Pod',
        'metadata': {
            'name': "minimal-notebook"
        },
        'spec': {
            'containers': [{
                'image': 'jupyter/minimal-notebook:latest',
                'name': 'minimal-notebook',
                'ports': [{
                    'containerPort': 8888    
                }]
            }]
        }
    }
    api.create_namespaced_pod(body=pod_manifest, namespace="default")

def create_service():
    service_manifest = {
        'apiVersion': 'v1',
        'kind': 'Service',
        'metadata': {
            'name': 'minimal-notebook'
        },
        'spec': {
            'selector': {
                'app': 'minimal-notebook'
            }
            'ports': {
                'protocol': "TCP",
                'port': 8888,
                'targetPort': 8888,
                'type': LoadBalancer
            }
        }
    }
    api.create(body=service_manifest, namespace="default")

def create_ingress():
    ingress_manifest = {
        'apiVersion': 'networking.k8s.io/v1',
        'kind': 'Ingress',
        'metadata':
            'name': 'minimal-ingress',
            'annotations':
                'nginx.ingress.kubernetes.io/rewrite-target': '/'
        'spec':
            'rules':
                'http':
                'paths':
                    'path': '/testpath',
                    'pathType': 'Prefix',
                    'backend':
                        'service':
                            'name': 'test',
                                'port':
                                    'number': '80'    
    networking_v1_beta1_api.create_namespaced_ingress(body=ingress_manifest, namespace="default")

def get_user():
    username = request.cookies.get('username')
    auth = request.cookies.get('auth')
    
    if username and auth:
        con = sqlite3.connect('app.db')
        cur = con.cursor()
        cur.execute("select username, cookie, token from users where username='%s' and cookie='%s'" % (username, auth))
        row = cur.fetchone()
        if row and row[0] == username and row[1] == auth:
            return row
    return None

@app.route("/create_notebook", methods=["GET"])
def create_notebook():
    user = get_user()
    # Create a token
    username = user[0]
    h = blake2b(key=secret_key, digest_size=digest_size)
    h.update(bytes(username, encoding="utf-8"))
    token = h.hexdigest()
    # Store token in database
    con = sqlite3.connect('app.db')
    cur = con.cursor()
    cur.execute("update users set token='%s' where username='%s'" % (token, username))
    con.commit()
    # Create a pod 
    create_pod()
    create_service()
    create_ingress()
    return render_template('index.html', username=username, token=token, authenticated=True)

@app.route("/register_view", methods=["GET"])
def register_view():
    return render_template('register.html')

@app.route("/register", methods=["POST"])
def register():
    username = request.json['username']
    password = request.json['password']
    con = sqlite3.connect('app.db')
    cur = con.cursor()
    cur.execute("select * from users where username='%s'" % username)
    if (cur.fetchone() == None):
        # Hash password
        h = blake2b(key=secret_key, digest_size=digest_size)
        h.update(bytes(password, encoding='utf-8'))
        passwordhash = h.hexdigest()
        # Insert user account information into database
        ts = str(datetime.datetime.now())
        query = "insert into users (username, password, token, create_ts, last_update_ts, cookie) values ('%s', '%s', '%s', '%s', '%s', '%s')" % (username, passwordhash, '', ts, ts, '')
        cur.execute(query)
        con.commit()
        return jsonify(status="okay")
    else:
        return jsonify(status="error", errorMessage="username already taken")

@app.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    # Hash password
    h = blake2b(key=secret_key, digest_size=digest_size)
    h.update(bytes(password, encoding='utf-8'))
    passwordhash = h.hexdigest()
    # Verify login
    con = sqlite3.connect('app.db')
    cur = con.cursor()
    cur.execute("select * from users where username='%s' and password='%s'" % (username, passwordhash))
    row = cur.fetchone()
    if (row[0] == username and row[1] == passwordhash):
        # Create a cookie
        h = blake2b(key=secret_key, digest_size=digest_size)
        h.update(bytes(username, encoding="utf-8"))
        cookie = h.hexdigest()
        # Update database with user cookie
        cur.execute("update users set cookie='%s' where username='%s'" % (cookie, username))
        con.commit()
        resp = make_response(render_template('index.html', authenticated=True))
        resp.set_cookie('username', username)
        resp.set_cookie('auth', cookie)
        return resp
    else:
        return render_template('index.html', authenticated=False)

@app.route("/")
def home():
    user = get_user()
    if user:
        return render_template('index.html', username=user[0], token=user[2], authenticated=True)
    return render_template('index.html', authenticated=False)

app.run(host='0.0.0.0', ssl_context=('./ssl/host.cert', './ssl/host.key'))