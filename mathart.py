import sys
import turtle

def hexagon(sidelength=100, left=True):
	if left:
		for i in range(6):
			turtle.forward(sidelength)
			turtle.left(60)
	else:
		for i in range(6):
			turtle.forward(sidelength)
			turtle.right(60)

def hexagonspiral(sidelength=100, left=True):
	if left:
		for i in range(72):
			hexagon(sidelength, left)
			turtle.left(5)
	else:
		for i in range(72):
			hexagon(sidelength, left)
			turtle.right(5)

def pentagon(sidelength=100, left=True):
	if left:
		for i in range(5):
			turtle.forward(sidelength)
			turtle.left(72)
	else:
		for i in range(5):
			turtle.forward(sidelength)
			turtle.right(72)

def pentagonspiral(sidelength=100, left=True):
	if left:
		for i in range(72):
			pentagon(sidelength, left)
			turtle.left(5)
	else:
		for i in range(72):
			pentagon(sidelength, left)
			turtle.right(5)

def star(sidelength=100, left=True):
	if left:
		for i in range(5):
			turtle.forward(sidelength)
			turtle.left(144)
	else:
		for i in range(5):
			turtle.forward(sidelength)
			turtle.right(144)

def starspiral(sidelength=100, left=True):
	if left:
		for i in range(1,73):
			star(i*5, left)
			turtle.left(5)
	else:
		for i in range(1,73):
			star(i*5, left)
			turtle.right(5)

def square(sidelength=100, left=True):
	if left:
		for i in range(4):
			turtle.forward(100)
			turtle.left(90)
	else:
		for i in range(4):
			turtle.forward(100)
			turtle.right(90)

def squarespiral(sidelength=100, left=True):
	if left:
		for i in range(72):
			square(sidelength, left)
			turtle.left(5) 
	else:
		for i in range(72):
			square(sidelength, left)
			turtle.right(5)

def triangle(sidelength=100, left=True):
	if left:
		for i in range(3):
			turtle.forward(sidelength)
			turtle.left(120)
	else:
		for i in range(3):
			turtle.forward(sidelength)
			turtle.right(120)

def trianglespiral(sidelength=100, left=True):
	if left:
		for i in range(72):
			triangle(sidelength, left)
			turtle.left(5)
	else:
		for i in range(72):
			triangle(sidelength, left)
			turtle.right(5)

if len(sys.argv) == 4:
	turtle.shape('turtle')
	locals()[sys.argv[1]](int(sys.argv[2]), sys.argv[3] == "left")
	turtle.done()