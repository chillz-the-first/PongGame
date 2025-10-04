from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):
    """Represents a paddle controlled by a player."""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5 ,stretch_len=1)
        self.goto(position[0], position[1])
        self.goto(position[0], position[1])

    def up(self):
        """Move paddle up, ensuring it doesn't leave screen."""
        new_y = self.ycor() + MOVE_DISTANCE
        if self.ycor() < 280:
            self.goto(self.xcor(), new_y)

    def down(self):
        """Move paddle down, ensuring it doesn't leave screen."""
        new_y = self.ycor() - MOVE_DISTANCE
        if self.ycor() > -280:
            self.goto(self.xcor(), new_y)


