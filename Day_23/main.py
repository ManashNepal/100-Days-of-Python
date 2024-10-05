import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

cars_list = []

screen.onkey(fun = player.move, key = "Up")

count = 0

game_is_on = True
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()

    if count%6 == 0:
        car = CarManager()
        cars_list.append(car)
    
    for each_car in cars_list:
        each_car.move()
    
    if player.has_cross_level():
        player.initial_position()
        car.increase_speed()
        scoreboard.next_level()
    
    for each_car in cars_list:
        if each_car.distance(player) < 25:
            print(each_car.distance(player))
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

    
    
    
