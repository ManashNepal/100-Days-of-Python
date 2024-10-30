from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POS = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.pieces = []
        self.create_snake()
        
    def create_snake(self):
        for pos in STARTING_POS:
            self.add_piece(pos)
        self.head = self.pieces[0]

    def reset(self):
        for piece in self.pieces:
            piece.goto(1000,1000)
        self.pieces.clear()
        self.create_snake()
        
    
    def add_piece(self,position):
        new_piece = Turtle(shape="square")
        new_piece.color("white")
        new_piece.penup()
        new_piece.goto(position)
        self.pieces.append(new_piece)

    def grow(self):
        last_piece = self.pieces[-1]
        new_position = last_piece.position()
        self.add_piece(new_position)


        # My logic
        # self.add_piece()
        # last_piece = self.pieces[-1]
        # x_pos = last_piece.xcor()
        # y_pos = last_piece.ycor()
        # if self.head.heading() == 90:
        #     self.snake_piece.goto(x_pos,y_pos-20)
        # elif self.head.heading() == 270:
        #     self.snake_piece.goto(x_pos,y_pos+20)
        # elif self.head.heading() == 0:
        #     self.snake_piece.goto(x_pos-20,y_pos)
        # elif self.head.heading() == 180:
        #     self.snake_piece.goto(x_pos+20,y_pos)
        # self.pieces.append(self.snake_piece)
    
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