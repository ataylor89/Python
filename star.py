import turtle

turtle.shape('turtle')


def star(sidelength=100):
    for i in range(5):
        turtle.forward(sidelength)
        turtle.right(144)

star(300)

turtle.done()
