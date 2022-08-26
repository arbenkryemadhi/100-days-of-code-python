from turtle import Turtle, Screen
import random


turtle = Turtle()
turtle.speed(0)
turtle.penup()
turtle.hideturtle()

screen = Screen()
screen.colormode(255)

dimensions = 10
dot_distance = 30
dot_size = 15
for _ in range(dimensions):
    for _ in range(dimensions):
        color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        turtle.dot(dot_size, color)
        turtle.forward(dot_distance)

    x_distance = dot_distance * dimensions
    turtle.goto(turtle.xcor() - x_distance, turtle.ycor() + dot_distance)

screen.exitonclick()
