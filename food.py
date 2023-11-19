from turtle import Turtle
from random import randint

WIDTH, LENGTH = 0.4, 0.4
START, END = -280, 280

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.shapesize(WIDTH, LENGTH)
        self.color("white")
        self.penup()
        self.relocate()

    def relocate(self):
        x_cor = randint(START, END)
        y_cor = randint(START, END)
        self.goto(x=x_cor, y=y_cor)