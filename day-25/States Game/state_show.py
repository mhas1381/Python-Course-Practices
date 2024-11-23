from turtle import Turtle

class Show(Turtle):
    def __init__(self , state , x , y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state = state
        self.x = x
        self.y = y
        self.show_location()
    def show_location(self):
        self.goto(self.x , self.y)
        self.write(f"{self.state}", align="center")
