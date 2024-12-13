FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-220,265)
        self.write_level()
    
    def write_level(self):
        self.write(f"Level: {self.level}",align="Center",font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write_level()
    
    def game_over(self):
        self.home()
        self.write("GAME OVER",align="Center",font=FONT)
