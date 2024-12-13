import turtle

my_turtle = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def move_right():
    my_turtle.right(10)

def move_left():
    new_heading = my_turtle.heading() + 10
    my_turtle.setheading(new_heading)

def clear():
    screen.reset()


screen.listen()

screen.onkeypress(key = "w", fun = move_forward)
screen.onkeypress(key = "d", fun = move_right)
screen.onkeypress(key = "a", fun = move_left)
screen.onkeypress(key = "s", fun = move_backward)
screen.onkeypress(key = "c", fun = clear)

screen.exitonclick()