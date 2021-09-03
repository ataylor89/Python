import turtle

turtle.shape('turtle')

def triangle(sidelength=100):
    for i in range(3):
        turtle.forward(sidelength)
        turtle.right(120)

triangle()
turtle.done()
