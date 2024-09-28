from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",18,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(0,270)
        self.display_score()
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_score()
        
    
    def display_score(self):
        self.write(arg=f"Score : {self.score}",move=False,align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        self.home()
        self.write(arg="Game Over.",move=False,align=ALIGNMENT,font=FONT)