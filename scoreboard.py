from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.update_screen()

    def increase_level(self):
        self.level += 1
        self.update_screen()
    def update_screen(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def determine_game(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)



