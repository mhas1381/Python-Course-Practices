from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def go_forward():
    timmy.forward(50)


def go_backward():
    timmy.backward(50)


def counter_clockwise():
    timmy.right(20)


def clockwise():
    timmy.left(20)


def clear_screen():
    screen.reset()


screen.listen()
screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.mainloop()
