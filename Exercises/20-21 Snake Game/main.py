from turtle import Turtle, Screen
from snake import Snake
import time


def main():
    # Screen setup.
    main_screen = Screen()
    main_screen.setup(width=600, height=600)
    main_screen.bgcolor("black")
    main_screen.title("Snake Game")
    main_screen.tracer(0)

    # Snake setup.
    snake = Snake()

    # Inputs.
    main_screen.listen()
    main_screen.onkey(snake.rotate_up, "Up")
    main_screen.onkey(snake.rotate_down, "Down")
    main_screen.onkey(snake.rotate_left, "Left")
    main_screen.onkey(snake.rotate_right, "Right")

    game_is_on = True
    while game_is_on:
        snake.move()

        # Updates frame.
        main_screen.update()
        time.sleep(0.1)

    main_screen.exitonclick()


if __name__ == "__main__":
    main()
