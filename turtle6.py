import turtle

for y in range(0, 3):

    for x in range(0, 3):
        turtle.penup()
        turtle.goto(x*30, y * 30)
        turtle.pendown()
        for n in range(0, 4):
            turtle.forward(10)
            turtle.right(90)

turtle.done()