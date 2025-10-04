from turtle import Turtle

class Ball(Turtle):
    """Represents the ball in the Pong game with movement and collision logic."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        """Move ball in current direction by x_move and y_move."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse vertical direction."""
        self.y_move *= -1

    def bounce_x(self):
        """
            Reverse horizontal direction and slightly increase speed
            to make the game gradually harder.
        """
        self.x_move *= -1
        if self.move_speed * 0.9 > 0:
            self.move_speed *= 0.9

    def reset_ball(self):
        """Return ball to center, reset speed, and reverse horizontal direction."""
        self.goto(0, 0)
        self.move_speed = 0.08
        self.bounce_x()
