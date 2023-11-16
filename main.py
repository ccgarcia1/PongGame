from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(position=350)
l_paddle = Paddle(position=-350)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "a")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('Y')

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce('X')

    #detect when the right paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.summarize_points(l_or_r='L')
        scoreboard.update_scoreboard()


    #detect when the left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.summarize_points(l_or_r='R')
        scoreboard.update_scoreboard()




screen.exitonclick()