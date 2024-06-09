from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    # "Step 1 : Create Turtle and it's location"
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("Green")
        self.penup()
        self.goto(STARTING_POSITION)

    # "Step 2 : Create user keys in order to move the Turtle"
    def move_turtle(self):

        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
