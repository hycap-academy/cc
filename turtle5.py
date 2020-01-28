import turtle

for x in range(0, 3):
    turtle.penup()
    turtle.goto(x*30, 0)
    turtle.pendown()
    for n in range(0, 4):
        turtle.forward(10)
        turtle.right(90)

turtle.done()