from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_turtle()
        self.reset_positions()
        self.goto_start()

    def create_turtle(self):
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)


    def goto_start(self):
        self.goto(STARTING_POSITION)
    def reset_positions(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False