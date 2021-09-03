import turtle

turtle.shape('turtle')

def star(sidelength=100):
    for i in range(5):
        turtle.forward(sidelength)
        turtle.right(144)

for i in range(1,73):
    star(i*5)
    turtle.right(5)

turtle.done()
