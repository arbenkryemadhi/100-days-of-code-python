from shutil import move
from turtle import Turtle
import time


MOVE_DISTANCE = 5


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto((-200, 0))
        self.x_direction = 1
        self.y_direction = 1

    def move(self):
        new_x = self.xcor() + MOVE_DISTANCE * self.x_direction
        new_y = self.ycor() + MOVE_DISTANCE * self.y_direction

        self.goto(new_x, new_y)

    def update(self):
        self.move()
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_direction *= -1
