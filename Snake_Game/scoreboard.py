from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",18,"bold")

# readFile = open("Day_20_21/high_score.txt", mode="r+")
# writeFile = open("Day_20_21/high_score.txt", mode="r+")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day_20_21/high_score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.setposition(0,270)
        self.display_score()
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.display_score()
        
    def display_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}  High Score: {self.high_score}",move=False,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day_20_21/high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.display_score()
