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

        # Detect collision with food.
        if snake.head.distance(food) <= 15:
            food.refresh()
            snake.extend()
            scoreboard.add_score(1)

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

        # Updates frame.
        main_screen.update()
        time.sleep(0.1)

    main_screen.exitonclick()


if __name__ == "__main__":
    main()