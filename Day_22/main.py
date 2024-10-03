from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()


screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

def can_bounce_on_paddle():
        global right_player_score, left_player_score
        if ball.distance(right_paddle) < 45:
            if ball.xcor() > 330:
               if ball.xcor() < 360:
                return True
        
        elif ball.distance(left_paddle) < 45:
            if ball.xcor() < -330:
              if ball.xcor() > -360:
                 return True
        else:
           return False
right_player_score = 0
left_player_score = 0

def paddle_miss():
    global left_player_score, right_player_score
    if ball.xcor() >= 390:
        scoreboard.l_score += 1
        return True
    elif ball.xcor() <= -390:
        scoreboard.r_score += 1
        return True
    else:
        return False

game_is_on = True

t1 = 0.1

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detection with wall
    if abs(ball.ycor()) >= 280:
        ball.bounce_wall()
    
    #Detection with both paddle
    if can_bounce_on_paddle():
        ball.bounce_paddle()
        t1 = 0.05
        
        
    #Detect when paddle misses
    if paddle_miss():
        scoreboard.write_score()
        ball.reset_ball()
            

screen.exitonclick()