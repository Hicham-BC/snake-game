import turtle as t
STARTING_POSTIONS = [(0, 0), (-10, 0), (-20, 0)]
WIDTH, LENGTH = 0.6, 0.6
UP, DOWN, RIGHT, LEFT = 90, 270, 0, 180
DISTANCE = 8

class Snake:
    def __init__(self):
        self.body = []
        self.create_body()
        self.head = self.body[0]
        

    def create_body(self):
        for position in STARTING_POSTIONS:
            segment = t.Turtle(shape="square")
            segment.penup()
            segment.shapesize(WIDTH, LENGTH)
            segment.setposition(position)
            self.body.append(segment)

    def move(self):
        for index in range(len(self.body) - 1, 0, -1):
            position = self.body[index - 1].pos()
            self.body[index].goto(position)
        
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)