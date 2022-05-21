import sys
import requests
from datetime import datetime
from dateutil import parser
import pprint as pp

def get_weather_report_for_today(latitude, longitude):
    weather_report = {}
    today = datetime.now().astimezone().strftime('%Y-%m-%d')
    full_report = get_weather_report(latitude, longitude)
    weather_report['meta'] = full_report['meta']
    if today in full_report:
        weather_report[today] = full_report[today]
    return weather_report

def get_weather_report_for(latitude, longitude, date):
    weather_report = {}
    full_report = get_weather_report(latitude, longitude)
    weather_report['meta'] = full_report['meta']
    if date in full_report:
        weather_report[date] = full_report[date]
    return weather_report

def get_weather_report(latitude, longitude):
    today = datetime.now().astimezone()
    weather_report = {
        'meta': {
            'time_of_report': today.strftime("%Y-%m-%d %H:%M:%S %Z"),
            'timezone': today.strftime('%Z'),
            'latitude': latitude,
            'longitude': longitude
        }
    }
    # Get the weather data from api.weather.gov
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    resp = requests.get(url)
    url = resp.json()['properties']['forecastGridData']
    resp = requests.get(url)
    # Reorganize the data into a JSON of our liking
    temp_data = resp.json()['properties']['temperature']
    dew_data = resp.json()['properties']['dewpoint']
    relhum_data = resp.json()['properties']['relativeHumidity']
    for reading in temp_data['values']:
        time_data = parse_valid_time(reading['validTime'])
        date = time_data['date']
        time = time_data['time']
        update_keys(weather_report, date, time)
        weather_report[date][time]['temp']['celsius'] = round(reading['value'], 1)
        weather_report[date][time]['temp']['fahrenheit'] = celsius_to_fahrenheit(reading['value'])
        weather_report[date][time]['temp']['period'] = time_data['period']
    for reading in dew_data['values']:
        time_data = parse_valid_time(reading['validTime'])
        date = time_data['date']
        time = time_data['time']
        update_keys(weather_report, date, time)
        weather_report[date][time]['dewpoint']['celsius'] = round(reading['value'], 1)
        weather_report[date][time]['dewpoint']['fahrenheit'] = celsius_to_fahrenheit(reading['value'])
        weather_report[date][time]['dewpoint']['period'] = time_data['period']
    for reading in relhum_data['values']:
        time_data = parse_valid_time(reading['validTime'])
        date = time_data['date']
        time = time_data['time']
        update_keys(weather_report, date, time)
        weather_report[date][time]['relative_humidity']['percent'] = reading['value']
        weather_report[date][time]['relative_humidity']['period'] = time_data['period']
    return weather_report

def update_keys(weather_report, date, time):
    if date not in weather_report:
        weather_report[date] = {}
    if time not in weather_report[date]:
        weather_report[date][time] = {
            'temp': {
                'celsius': None,
                'fahrenheit': None,
                'period': None
            }, 
            'dewpoint': {
                'celsius': None,
                'fahrenheit': None,
                'period': None
            },
            'relative_humidity': {
                'percent': None,
                'period': None
            }
        }

def parse_valid_time(valid_time):
    dt = valid_time.split("/PT")[0]
    dt = parser.parse(dt).astimezone()
    return {
        'date': dt.strftime("%Y-%m-%d"),
        'time': dt.strftime("%H:%M:%S"),
        'period': valid_time.split("/PT")[1]
    }

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def main():
    if len(sys.argv) < 3:
        print("Usage: python %s <latitude> <longitude>" %sys.argv[0])
        return
    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    weather_report = get_weather_report_for_today(latitude, longitude)
    pp.pprint(weather_report)

if __name__ == '__main__':
    main()