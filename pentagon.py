import turtle

turtle.shape('turtle')

def pentagon(sidelength=100, facing_up=True):
    if facing_up:
        for i in range(5):
            turtle.forward(sidelength)
            turtle.left(72)
    else:
        for i in range(5):
            turtle.forward(sidelength)
            turtle.right(72)

pentagon()
turtle.done()
