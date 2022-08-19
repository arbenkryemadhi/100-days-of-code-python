from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0


class Snake:
    def __init__(self):
        # Snake segments.
        self.segments = []
        self.DO_NOT_CALL_create_snake()
        self.head = self.segments[0]

    def DO_NOT_CALL_create_snake(self):
        # Snake setup.
        for pos in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.goto(pos)
            new_segment.color("white")
            self.segments.append(new_segment)

    def move(self):
        # Moves each segment like a chain.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def rotate_up(self):
        if self.head.heading() != DOWN_DIRECTION:
            self.head.setheading(UP_DIRECTION)

    def rotate_down(self):
        if self.head.heading() != UP_DIRECTION:
            self.head.setheading(DOWN_DIRECTION)

    def rotate_left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.setheading(LEFT_DIRECTION)

    def rotate_right(self):
        if self.head.heading() != LEFT_DIRECTION:
            self.head.setheading(RIGHT_DIRECTION)
