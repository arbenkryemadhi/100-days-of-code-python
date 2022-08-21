from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer()

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()

    screen.listen()
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")

    is_game_on = True
    while is_game_on:
        ball.update()
        screen.update()
        time.sleep(0.01)

    screen.exitonclick()


if __name__ == "__main__":
    main()
