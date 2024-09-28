from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
import random
from scoreboard import Scoreboard

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

game_still_on = True
while game_still_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Collison with food
    if snake.head.distance(food)  < 15:
        food.refresh()
        snake.grow()
        scoreboard.update_score()
    
    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_still_on = False
        scoreboard.game_over()
    
    # Collision with Tail
    for n in range(1,len(snake.pieces)-1):
        if snake.head.distance(snake.pieces[n])<15:
            print(snake.head.distance(snake.pieces[n]))
            game_still_on = False
            scoreboard.game_over()


screen.exitonclick()