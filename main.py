from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
#screen.tracer(0)
r_paddle = Paddle(position=350)
l_paddle = Paddle(position=-350)

ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "a")




screen.exitonclick()