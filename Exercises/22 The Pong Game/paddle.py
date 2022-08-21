from turtle import Turtle


MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
