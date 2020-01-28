import turtle
import random


turtle.speed(10)
for x in range(0, 1000):

    size = random.randint(10,100)
    angle = random.randint(0,90)

    r= random.random()
    g= random.random()
    b= random.random()
    
    turtle.pencolor(r,g,b)
    turtle.penup()
    turtle.goto(random.randint(-400,400), random.randint(-400,400))
    turtle.pendown()

    turtle.right(angle)
    for n in range(0, 4):
            turtle.forward(size)
            turtle.right(90)

