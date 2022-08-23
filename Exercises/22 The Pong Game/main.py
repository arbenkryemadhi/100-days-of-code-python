from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
    scoreboard = Scoreboard()
    scoreboard.write_score()

    screen.listen()
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")

    is_game_on = True
    while is_game_on:
        time.sleep(0.01)

        if ball.xcor() > 380:
            scoreboard.increase_score_for("left")
        elif ball.xcor() < -380:
            scoreboard.increase_score_for("right")

        ball.update(r_paddle, l_paddle)
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
