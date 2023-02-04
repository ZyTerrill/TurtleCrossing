from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
car_count = 6
road1_start_y = -225
road1_end_y = -175
road2_start_y = -139
road2_end_y = -89
road3_start_y = -53
road3_end_y = -3
road4_start_y = 33
road4_end_y = 83
road5_start_y = 119
road5_end_y = 169
road6_start_y = 205
road6_end_y = 255
road1cars = []


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 3)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=0.5, stretch_len=1.3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y1 = random.randint(road1_start_y, road1_end_y)
            random_y2 = random.randint(road2_start_y, road2_end_y)
            random_y3 = random.randint(road3_start_y, road3_end_y)
            random_y4 = random.randint(road4_start_y, road4_end_y)
            random_y5 = random.randint(road5_start_y, road5_end_y)
            random_y6 = random.randint(road6_start_y, road6_end_y)
            random_y_list = [random_y1, random_y2, random_y3, random_y4, random_y5, random_y6]
            random_y = random.choice(random_y_list)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def clear_car(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                car.hideturtle()

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        self.clear_car()

    def level_up(self):
        self.car_speed += 5
