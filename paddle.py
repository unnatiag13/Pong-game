from turtle import Turtle
import random

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(pos)

    def go_up(self):
        y = self.ycor()+20
        self.goto(self.xcor(),y=y)

    def go_down(self):
        y = self.ycor()-20
        self.goto(self.xcor(),y=y)







class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def bouncey(self):
        self.ymove *= -1

    def bouncex(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def miss(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bouncex()
        self.move()