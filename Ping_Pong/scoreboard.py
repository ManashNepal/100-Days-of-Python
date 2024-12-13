from turtle import Turtle

FONT = ("Courier",50,"bold")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}", align=ALIGN, font= FONT)
        self.goto(100,200)
        self.write(f"{self.r_score}", align=ALIGN, font= FONT)

        