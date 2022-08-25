from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
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
        self.score = 0
        self.draw_score()
