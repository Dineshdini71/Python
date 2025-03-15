from  turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.go_to()
        self.lt(90)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def go_to(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

