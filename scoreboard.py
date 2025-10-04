from turtle import Turtle

class Scoreboard(Turtle):
    """Tracks and displays scores for both players."""
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score_p1 = 0
        self.score_p2 = 0
        self.goto(0, 265)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        """Clear previous score and write the updated score at top-center."""
        self.clear()
        self.write(f"{self.score_p2} : {self.score_p1}", align="center", font=("Courier", 30, "normal"))

    def increase_score(self, p):
        """
            Increment score for a given player.
            player = 1 → right player
            player = 2 → left player
        """
        if p == 1:
            self.score_p1 += 1
        elif p == 2:
            self.score_p2 += 1
        self.display_score()
