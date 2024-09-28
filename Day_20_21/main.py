from turtle import Screen
import time
from snake import Snake
from food import Food
import random

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

game_still_on = True
while game_still_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food)  < 15:
        print(snake.head.distance(food))
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        food.goto(random_x, random_y)


screen.exitonclick()