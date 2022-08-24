import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    # Difficulty settings.
    difficulty_level = 10
    num_of_cars_to_create = 1

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(player.go_up, "Up")

    game_is_on = True
    while game_is_on:
        for _ in range(50):
            car_manager.create_cars(
                number_of_cars_to_create=num_of_cars_to_create)
            for _1 in range(difficulty_level):
                time.sleep(0.1)
                screen.update()
                car_manager.update()

        if difficulty_level > 5:
            difficulty_level -= 1
        else:
            num_of_cars_to_create += 1


if __name__ == "__main__":
    main()
