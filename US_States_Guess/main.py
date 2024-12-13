import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

turtle.addshape("blank_states_img.gif") 
turtle.shape("blank_states_img.gif")

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()

guessed_list = []
correct_guess = 0
still_on = True

while correct_guess < 51:
    user_guess = screen.textinput(title=f"{correct_guess}/50 States Correct",prompt="What's another state's name?: ").title()
    if user_guess == "Exit":
        for state in guessed_list:
            states_list.remove(state) 
        break
    if user_guess in states_list and user_guess not in guessed_list:
        correct_guess += 1
        guessed_list.append(user_guess)
        # Creating Turtle to write
        my_turtle = turtle.Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        row = states_data[states_data["state"] == user_guess]
        x_cor = row.iloc[0,1]
        y_cor = row.iloc[0,2]
        my_turtle.goto(x=x_cor,y=y_cor)
        my_turtle.write(user_guess, font=("Courier",8,"bold"))

states_to_learn = pandas.DataFrame({"State" : states_list})

states_to_learn.to_csv("states_to_learn.csv")

# screen.exitonclick()