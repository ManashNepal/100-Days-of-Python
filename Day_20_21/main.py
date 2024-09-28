from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
import random
from scoreboard import Scoreboard
from special_food import SpecialFood

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
scoreboard = Scoreboard()


def over():
    global game_still_on
    game_still_on = False
    scoreboard.game_over()

count = 0
game_still_on = True
while game_still_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    # Collison with food - 1pt.
    if snake.head.distance(food)  < 15:
        food.refresh()
        snake.grow()
        scoreboard.update_score()
        count += 1
        
    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        over()
    
    # Collision with Tail
    for piece in snake.pieces[1:]:
        if snake.head.distance(piece) < 10:
            over()


screen.exitonclick()