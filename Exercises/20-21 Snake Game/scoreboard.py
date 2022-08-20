from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.score = 0
        self.goto(0, 250)

    def add_score(self, scoreIncrease: int):
        self.score += scoreIncrease

    def draw_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center",
                   font=("Arial", 25, "normal"))
