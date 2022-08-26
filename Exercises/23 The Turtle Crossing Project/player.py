from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.go_to_starting_position()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_starting_position(self):
        self.goto(STARTING_POSITION)

    def passed_finished_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

        return False

    def update():
        pass
