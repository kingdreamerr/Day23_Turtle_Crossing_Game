from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        make_car = random.randint(1, 6)
        if make_car == 1:
            new_car = Turtle("square")
            # new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2.5, 0.1)
            new_car.penup()
            random_position = random.randint(-250, 250)
            new_car.goto(300, random_position)
            self.all_cars.append(new_car)

    def set_location(self):
        random_position = random.randint(-250, 250)
        self.goto(300, random_position)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
    