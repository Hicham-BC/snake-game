from turtle import Turtle
from random import randrange

WIDTH, LENGTH = 0.4, 0.4
START, END, STEP = -280, 280, 10

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.shapesize(WIDTH, LENGTH)
        self.color("white")
        self.penup()
        self.relocate()

    def relocate(self):
        x_cor = randrange(START, END, STEP)
        y_cor = randrange(START, END, STEP)
        self.goto(x=x_cor, y=y_cor)