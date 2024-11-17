# import colorgram
from random import choice
from turtle import Turtle,Screen
timmy = Turtle()
screen = Screen()
# colors = colorgram.extract('image.jpg' , 12)
# for color in colors:
#     colors_rgb.append(tuple(color.rgb))
# print(colors_rgb)
timmy.penup()
colors = ["red" , "blue" , "brown" , "yellow" , "pink"]
# timmy.setheading(225)
# timmy.forward(300)
# timmy.setheading(0)
# colors_rgb = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73)]
y = 0
for dot in range(101):
    timmy.color(choice(colors))
    timmy.forward(50)
    timmy.dot(20)
    if dot > 1 and dot % 10 ==0:
        y += 50
        timmy.setx(0)
        timmy.sety(y)
timmy.setheading(90)
screen.mainloop()