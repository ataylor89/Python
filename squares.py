import turtle

turtle.shape('turtle')

def square(sidelength=100):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)

square(50)
square(30)
square(100)

turtle.done()
