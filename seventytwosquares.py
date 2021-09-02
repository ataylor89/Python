import turtle

def square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

for i in range(72):
    square()
    turtle.right(5)                

turtle.done()
