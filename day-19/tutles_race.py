from random import choice,randint
from turtle import Turtle,Screen
from tkinter import messagebox
colors = ['red' , 'blue' , 'yellow' , 'purple' , 'brown' , 'orange']

screen = Screen()
screen.setup(height=500 , width=500)
user_guess = screen.textinput("Race" , "Who win the race?")
x = -240
y = -170
game_is_going = True
turtles = []
for _ in range(6):
    new_turtle = Turtle(shape='turtle')
    color = choice(colors)
    new_turtle.color(color)
    colors.remove(color)
    new_turtle.penup()
    new_turtle.goto(x , y)
    y += 60
    turtles.append(new_turtle)
while game_is_going:
    for turtle in turtles:
        turtle.forward(randint(10 , 40))
        if turtle.xcor() > 230:
            winner = turtle.color()[0]
            if user_guess == winner:
                messagebox.showinfo("showinfo", f"You win!\nThe winner is {winner}")
            else:
                messagebox.showinfo("showinfo", f"You lose!\nThe winner is {winner}")

            game_is_going = False







screen.mainloop()
