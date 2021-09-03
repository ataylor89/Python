import turtle

turtle.shape('turtle')

def square(sidelength, direction='R'):
    if direction == 'R':
        for i in range(4):
            turtle.forward(sidelength)
            turtle.right(90)
    else:
        for i in range(4):
            turtle.forward(sidelength)
            turtle.left(90)
        
for i in range(1, 73):
    square(i*5)
    turtle.right(5)

turtle.done()
