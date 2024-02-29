import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Turtle Crossing Game")
screen.tracer(0)
all_cars = []
car_speed = 0.1
# get_random_number_of_car = random.choice(range(5, 15))
player = Player()
scoreboard = Scoreboard()
player_distance = player.position()

screen.listen()
screen.onkey(player.move, "Up")

for _ in range(15):
    cars = CarManager()
    cars.car_colours()
    all_cars.append(cars)

game_is_on = True
while game_is_on:
    screen.update()
    for car in all_cars:
        car.move()

        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.determine_game()
        elif player.ycor() > 290:
            player.goto(0, -290)
            scoreboard.increase_level()
            car.increase_speed()
    if player.ycor() > 290:
        player.goto(0, -280)
        scoreboard.increase_level()
        # car_speed -= 0.01

    if random.randint(1, 10) == 1:
        new_car = CarManager()
        new_car.car_colours()
        all_cars.append(new_car)

    time.sleep(car_speed)

screen.exitonclick()
