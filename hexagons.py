import turtle

def hexagon(sidelength=100):
    for i in range(6):
        turtle.forward(sidelength)
        turtle.right(60) 

for i in range(72):
    hexagon(100)
    turtle.right(5)

turtle.done()      
