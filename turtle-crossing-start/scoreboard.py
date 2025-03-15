from turtle import Turtle

ALIGN = 'left'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.level = 0
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)

