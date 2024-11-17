from random import choice, randint
from turtle import Turtle, Screen

timmy = Turtle()
# timmy.shape("square")
timmy.color("blue")
# timmy.colormode(255)
timmy.speed("fastest")
colors = ["red" , "blue" , "brown" , "yellow" , "pink"]


def generate_random_color():
    r = randint(255)
    g = randint(255)
    b = randint(255)
    rgb_tuple = (r , g , b)
    return rgb_tuple


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

## Random walk
# directions = [0, 90, 180, 270]
# timmy.speed(10)
# timmy.pensize(10)
#
# for _ in range(100):
#     timmy.color(choice(colors))
#     timmy.forward(15)
#     timmy.setheading(choice(directions))

## Draw a Spirograph

angle = 0
for _ in range(72):
    timmy.color(choice(colors))
    timmy.circle(100)
    timmy.setheading(angle)
    angle += 5


screen = Screen()
screen.mainloop()
