from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open(file=os.path.join(os.sys.path[0], "data.txt"), mode="r") as data:
            self.high_score = int(data.read())
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.draw_score()

    def add_score(self, scoreIncrease: int):
        self.score += scoreIncrease
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file=os.path.join(os.sys.path[0], "data.txt"), mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.draw_score()
