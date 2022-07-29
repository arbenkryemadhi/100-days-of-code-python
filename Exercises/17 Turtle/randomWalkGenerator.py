from turtle import Turtle, Screen, distance
import random
from random import choice


turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()
turtle.width(3)

screen = Screen()

directions = [0, 90, 180, 270]

for _ in range(1000):
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.right(choice(directions))
    turtle.forward(10)


screen.exitonclick()
