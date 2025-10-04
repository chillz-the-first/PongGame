from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score_p1 = 0
        self.score_p2 = 0
        self.goto(0, 280)
        # self.pendown()
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.score_p2} : {self.score_p1}", align="center", font=("Courier", 16, "normal"))

    def increase_score(self, p):
        if p == 1:
            self.score_p1 += 1
        elif p == 2:
            self.score_p2 += 1
        self.display_score()