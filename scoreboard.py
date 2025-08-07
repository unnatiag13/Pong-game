from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score=0
        self.r_score=0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,False,"center",("courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,False,"center",("courier",80,"normal"))

    def lpoint(self):
        self.l_score+=1
        self.update_score()

    def rpoint(self):
        self.r_score+=1
        self.update_score()