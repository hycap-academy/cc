import turtle

for x in range(0, 9):

    for n in range(0, 4):
        turtle.forward(100)
        turtle.right(90)

    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()

turtle.done()