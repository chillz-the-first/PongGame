from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

p1 = Paddle((350, 0))           #Right paddle
p2 = Paddle((-350, 0))          #Left paddle
ball = Ball()
score = Scoreboard()

screen.listen() #listen to keystrokes
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")
screen.onkey(p2.up, "w")
screen.onkey(p2.down, "s")

def side_collision():
    x= ball.xcor()
    y= ball.ycor()
    if y > 280 or y < -280:
        ball.bounce_y()

def paddle_collision():
    # if ball.distance(p1) < 33 and ball.xcor() > 335 or ball.distance(p2) < 33 and ball.xcor() < -335:
    #     print("Paddle Collision")
    #     ball.bounce_x()

    # Right paddle collision
    if (p1.xcor() - 10 < ball.xcor() + 10 < p1.xcor() + 10) and (p1.ycor() - 50 < ball.ycor() < p1.ycor() + 50):
        ball.bounce_x()

    #p1.xcor() - 10 → left edge of right paddle
    #p1.xcor() + 10 → right edge of right paddle
    #ball.xcor() + 10 → right edge of ball (radius = 10); Similarly for y coordinates

    # Left paddle collision
    if (p2.xcor() - 10 < ball.xcor() - 10 < p2.xcor() + 10) and (p2.ycor() - 50 < ball.ycor() < p2.ycor() + 50):
        ball.bounce_x()

def wall_collision():
    #Right wall collision
    if ball.xcor() > p1.xcor() + 20:
        ball.goto(0,0)
        score.increase_score(2)
        ball.reset_ball()
    #Left wall collision
    elif ball.xcor() < p2.xcor() - 20:
        ball.goto(0,0)
        score.increase_score(1)
        ball.reset_ball()


game_is_on = True
while game_is_on:
    time.sleep(0.06)
    screen.update()

    ball.move()
    side_collision()
    paddle_collision()
    wall_collision()




screen.exitonclick()
