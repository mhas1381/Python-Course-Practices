import turtle
from state_show import Show
import pandas

screen = turtle.Screen()
screen.title("States Game")
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
number_guessed = 0

game_is_continue = True

while game_is_continue:
    answer_state = turtle.textinput(f"{number_guessed}/{len(states)} Guess the State",
                                    "What's the another state's name:").title()

    if answer_state in states:
        location = data[data.state == answer_state]
        x = int(location.x.iloc[0])
        y = int(location.y.iloc[0])
        show_state = Show(answer_state, x, y)
        number_guessed += 1
    elif answer_state == "Exit":
        game_is_continue = False

screen.mainloop()
