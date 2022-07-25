from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(x=-200, y=250)

    def write_score(self, score, mistakes):
        self.clear()
        self.write(f"SCORE: {score}     MISTAKES: {mistakes}", align=ALIGN, font=FONT)