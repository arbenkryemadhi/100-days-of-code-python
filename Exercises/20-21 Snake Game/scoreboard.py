from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.draw_score()

    def add_score(self, scoreIncrease: int):
        self.score += scoreIncrease
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT,
                   font=FONT)
