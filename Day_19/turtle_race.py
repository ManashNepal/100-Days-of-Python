from turtle import Turtle, Screen
import random

screen = Screen()
turtle1 = Turtle(shape="turtle")
turtle2 = Turtle(shape="turtle")
turtle3 = Turtle(shape="turtle")
turtle4 = Turtle(shape="turtle")
turtle5 = Turtle(shape="turtle")
turtle6 = Turtle(shape="turtle")

turtles = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6]
colors= ["red", "orange", "yellow", "green", "blue", "purple"]

screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet",prompt="Who will win the race? Enter color: ")

#Checks if input is given or not. Prompts again if not given
if not user_bet:
    user_bet = screen.textinput(title="Make your bet",prompt="You need to enter your bet! Enter color: ")

i = 0
y_cor = -60
for turtle in turtles:
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-230, y=y_cor)
    i += 1
    y_cor += 30


is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You won! The {winner} turtle won the race")
            else:
                print(f"You lost! The {winner} turtle won the race")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()