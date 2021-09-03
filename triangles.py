import turtle

turtle.shape('turtle')

def triangle(sidelength=100):
    for i in range(3):
        turtle.forward(sidelength)
        turtle.right(120)

for i in range(72):
    triangle()
    turtle.right(5)

turtle.done()
