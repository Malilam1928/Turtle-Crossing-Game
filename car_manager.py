from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 20


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_increment = 0

    def create_random_car(self):
        random_coeff = random.randint(1, 6)
        if random_coeff == 1:
            new_car = Turtle()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.move_increment += MOVE_INCREMENT
