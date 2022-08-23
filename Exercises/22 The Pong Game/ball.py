from turtle import Turtle
import random
import time


MOVE_DISTANCE = 5


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto((0, 0))
        self.x_direction = random.randrange(-1, 2, 2)
        self.y_direction = random.randrange(-1, 2, 2)

    def move(self):
        new_x = self.xcor() + MOVE_DISTANCE * self.x_direction
        new_y = self.ycor() + MOVE_DISTANCE * self.y_direction

        self.goto(new_x, new_y)

    def win(self):
        if self.xcor() < 390 and self.xcor() > -390:
            return

        self.goto((0, 0))
        time.sleep(1)
        self.y_direction *= random.randrange(-1, 2, 2)

    def bounce(self, r_paddle, l_paddle):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_direction *= -1

        if self.distance(r_paddle) < 50 and self.xcor() > 330:
            self.x_direction *= -1
        elif self.distance(l_paddle) < 50 and self.xcor() < -330:
            self.x_direction *= -1

    def update(self, r_paddle, l_paddle):
        self.move()
        self.bounce(r_paddle, l_paddle)
        self.win()
