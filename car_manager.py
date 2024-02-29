from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

    def move(self):
        self.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.backward(STARTING_MOVE_DISTANCE + 5)

    def car(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        x = random.randint(270, 300)
        y = random.randint(-240, 250)
        x_move = self.xcor() + x
        y_move = self.ycor() + y
        self.goto(x_move, y_move)

    def car_colours(self):
        self.color(random.choice(COLORS))
        self.car()

    def get_more_car(self, cars):
        pass



