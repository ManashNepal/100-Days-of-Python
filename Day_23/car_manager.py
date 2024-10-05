import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SPEED = STARTING_MOVE_DISTANCE


class CarManager(Turtle):
    def __init__(self):
        super().__init__()    
        self.shape("square")
        self.color(random.choice(COLORS))
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(300,random.randint(-250,250))
        

    def increase_speed(self):
        global CAR_SPEED
        CAR_SPEED += MOVE_INCREMENT
    
    def move(self):
        self.forward(CAR_SPEED)

        
        
    
    
    
