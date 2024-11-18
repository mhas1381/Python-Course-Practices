from turtle import Turtle
class Paddle(Turtle):
    def __init__(self , position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def up(self):
        y = self.ycor()
        self.sety(y + 20)


    def down(self):
        y = self.ycor()
        self.sety(y - 20)
