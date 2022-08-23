import string
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.l_score = 0
        self.r_score = 0

    def write_score(self):
        self.clear()
        # Right score:
        self.goto(100, 175)
        self.write(self.r_score, align="center",
                   font=("Courier", 80, "normal"))

        # Left score:
        self.goto(-100, 175)
        self.write(self.l_score, align="center",
                   font=("Courier", 80, "normal"))

    def increase_score_for(self, l_or_r: string):
        if l_or_r.lower() == "left":
            self.l_score += 1
        elif l_or_r.lower() == "right":
            self.r_score += 1

        self.write_score()
