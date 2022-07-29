from turtle import Turtle, Screen


turtle1 = Turtle()
screen = Screen()


def move_forwards():
    turtle1.forward(10)


def move_backwards():
    turtle1.forward(-10)


def rotate_clockwise():
    turtle1.right(3)


def rotate_counterclockwise():
    turtle1.right(-3)


def clear_screen():
    turtle1.home()
    turtle1.clear()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=rotate_clockwise, key="d")
screen.onkey(fun=rotate_counterclockwise, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
