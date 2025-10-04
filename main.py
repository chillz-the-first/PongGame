from turtle import Screen, Turtle
from paddles import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

p1 = Paddle("right")
p2 = Paddle("left")

screen.listen() #listen to keystrokes
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")
screen.onkey(p2.up, "w")
screen.onkey(p2.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(0.05)





screen.exitonclick()
