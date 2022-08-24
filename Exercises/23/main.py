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
    scoreboard = Scoreboard()

    scoreboard.update_score()

    screen.listen()
    screen.onkey(player.go_up, "Up")

    spawn_counter = 11
    difficulty_counter = 0
    game_is_on = True
    while game_is_on:
        # Game Over!
        for car in car_manager.cars_list:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()
                break

        # Detect a successful crossing.
        if player.passed_finished_line():
            player.go_to_starting_position()
            car_manager.level_up()
            scoreboard.update_score()

        # Spawn cars settings.
        if spawn_counter > difficulty_level:
            car_manager.create_cars(
                number_of_cars_to_create=num_of_cars_to_create)
            spawn_counter = 0

        # Difficulty settings.
        if difficulty_counter > 50:
            if difficulty_level > 5:
                difficulty_level -= 1
            else:
                num_of_cars_to_create += 1
            difficulty_counter = 0

        # Main Update Function
        screen.update()
        car_manager.update()
        spawn_counter += 1
        difficulty_counter += 1
        time.sleep(0.1)

    screen.exitonclick()


if __name__ == "__main__":
    main()
