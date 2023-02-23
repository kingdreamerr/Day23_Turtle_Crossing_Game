from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # self.color("")
        self.score = 0
        self.goto(-255, 250)
        self.update_screen()
