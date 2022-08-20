from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
    food = Food()
    scoreboard = Scoreboard()

    # Inputs.
    main_screen.listen()
    main_screen.onkey(snake.rotate_up, "Up")
    main_screen.onkey(snake.rotate_down, "Down")
    main_screen.onkey(snake.rotate_left, "Left")
    main_screen.onkey(snake.rotate_right, "Right")

    game_is_on = True
    while game_is_on:
        snake.move()
        scoreboard.draw_score()

        # Detect collision.
        if snake.head.distance(food) <= 15:
            food.refresh()
            scoreboard.add_score(1)

        # Updates frame.
        main_screen.update()
        time.sleep(0.05)

    main_screen.exitonclick()


if __name__ == "__main__":
    main()
