from turtle import Turtle,Screen
import random
import time
from scoreboard import Scoreboard
from paddle import Paddle,Ball

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

gameOn=True
while gameOn:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # deetcting collisions with upper and lower wall
    if ball.ycor()>278 or ball.ycor()<-278:
        ball.bouncey()

    #detect collision with paddle.
    if ball.xcor()>320 and ball.distance(r_paddle)<50 or ball.xcor()<-320 and ball.distance(l_paddle)<50:
        ball.bouncex() 

    #detect when the R paddle misses the ball
    if ball.xcor()>400 :
        ball.miss()
        score.lpoint()
    
    #detect when the L paddle misses the ball
    if ball.xcor()<-400 :
        ball.miss()
        score.rpoint()

screen.exitonclick()
