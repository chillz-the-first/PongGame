from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
ball = Ball()

screen.listen() #listen to keystrokes
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")
screen.onkey(p2.up, "w")
screen.onkey(p2.down, "s")

def wall_collision():
    x= ball.xcor()
    y= ball.ycor()
    if y > 280 or y < -280:
        ball.bounce()


game_is_on = True
while game_is_on:
    time.sleep(0.06)
    screen.update()
    ball.move()
    wall_collision()




screen.exitonclick()
