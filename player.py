from turtle import  Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.seth(90)
        # self.upward_move = 0

    def move(self):
        self.forward(MOVE_DISTANCE)
        self.xcor() + MOVE_DISTANCE
