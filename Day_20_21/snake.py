from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    pieces = []
    def __init__(self):
        starting_pos = [(0,0), (-20,0), (-40,0)]
        for pos in starting_pos:
            snake_piece = Turtle(shape="square")
            snake_piece.color("white")
            snake_piece.penup()
            snake_piece.goto(pos)
            self.pieces.append(snake_piece)
        self.head = self.pieces[0]
    
    def move(self):
        for n in range(len(self.pieces)-1, 0, -1):
            new_pos = self.pieces[n-1].position()
            self.pieces[n].setposition(new_pos)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)