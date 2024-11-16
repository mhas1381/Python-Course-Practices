from random import choice
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

## Draw a Square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

## Draw a dashed line
# for _ in range(100):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Draw Different shapes
# def draw_shape(num_sides):
#     colors = ["red" , "blue" , "brown" , "yellow" , "pink"]
#     angle = 360 / num_sides
#     timmy.color(choice(colors))
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)



screen = Screen()
screen.mainloop()
