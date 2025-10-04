from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        # self.color("white")
        self.shapesize(stretch_wid=5 ,stretch_len=1)
        self.position = position
        if position == "right":
            self.goto(350, 0)
            self.color("red")
        else:
            self.goto(-350, 0)
            self.color("blue")

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if self.ycor() < 250:
            if self.position == "right":
                self.goto(350, new_y)
            else:
                self.goto(-350, new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if self.ycor() > -250:
            if self.position == "right":
                self.goto(350, new_y)
            else:
                self.goto(-350, new_y)


