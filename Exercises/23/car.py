import string
from turtle import Turtle


class Car(Turtle):
    def __init__(self, position: tuple, color: string) -> None:
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(position)
        self.setheading(180)

    def move(self, move_distance):
        self.forward(move_distance)
