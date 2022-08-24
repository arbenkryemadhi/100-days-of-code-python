import random
import time
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        # List of car objects
        self.cars_list = []

        # Car's starting x and y position and color which will be randomized later.
        self.current_x_car_spawn_pos = 310
        self.current_y_car_spawn_pos = 0
        self.car_color = ""

    def create_cars(self, number_of_cars_to_create: int):
        for _ in range(number_of_cars_to_create):
            # X position is randomized from a right point, going left or right.
            self.current_x_car_spawn_pos += (random.randint(0, 100))

            # Y position is randomized from 0, going up or down.
            self.current_y_car_spawn_pos += (random.randint(-280, 280))

            # Randomizes color.
            self.car_color = random.choice(COLORS)

            # Crate
            car = Car(
                position=(self.current_x_car_spawn_pos, self.current_y_car_spawn_pos), color=self.car_color)

            # Adds car to the car list.
            self.cars_list.append(car)

            # Rest x and y position for next car.
            self.current_x_car_spawn_pos = 280
            self.current_y_car_spawn_pos = 0

    def update(self):
        for car in self.cars_list:
            car.move(move_distance=STARTING_MOVE_DISTANCE)
