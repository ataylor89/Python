import turtle

turtle.shape('turtle')

def polygon(n=6, l=100, direction='L'):
    if direction == 'L':
        for i in range(n):
            turtle.forward(l)
            turtle.left(360/n)
    else:
        for i in range(n):
            turtle.forward(l)
            turtle.right(360/n)

polygon(100, 10, 'R')

turtle.done()
