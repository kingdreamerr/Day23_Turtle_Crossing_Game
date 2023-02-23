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

    def update_screen(self):
        self.clear()
        self.write(f"Score:{self.score}", align='left', font=FONT)

    def add_score(self):
        self.score += 1
        self.update_screen()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align='center', font=FONT)