from turtle import Turtle, Screen
import random
import turtle 


# import colorgram
# colors = colorgram.extract('Day_18/image.jpg',30)

# color_list = []

# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     temp_color = (r, g, b)
#     color_list.append(temp_color)

# print(color_list)

color_list = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

turtle.colormode(255)
my_turtle = Turtle()
screen = Screen()

my_turtle.speed("fastest")

# Setting to a specific position
my_turtle.penup()
my_turtle.setposition(-240,-200)


def go_to_initial():
    # my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    for _ in range(9):
        my_turtle.forward(50)
    my_turtle.right(180)

def draw():
    for _ in range(9):
        my_turtle.dot(17, random.choice(color_list))
        my_turtle.forward(50)  
    my_turtle.dot(17, random.choice(color_list))


for _ in range(9):
    draw()
    go_to_initial()
draw()



screen.exitonclick()