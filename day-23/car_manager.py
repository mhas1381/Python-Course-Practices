from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1 ,stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(300 , randint(-250 , 250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
            self.car_speed += MOVE_INCREMENT
