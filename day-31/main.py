from tkinter import *
import pandas
from pandas.core.methods.to_dict import to_dict
from random import choice

############################## Words ##################################
try:
    data = pandas.read_csv('data/to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')

words_dic = to_dict(data, orient='records')

current_card = {}


def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_dic)
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=fr_img)
    canvas.itemconfig(title, text="French", fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(canvas_image, image=en_img)


def is_known():
    words_dic.remove(current_card)
    remining_words = pandas.DataFrame(words_dic)
    remining_words.to_csv('data/to_learn', index=False)
    change_word()


############################## UI Setup ##############################
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

fr_img = PhotoImage(file="images/card_front.png")
en_img = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(0, 0, image=fr_img, anchor='nw')

canvas.grid(row=0, column=0, columnspan=2)

title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

wrong_btn = Button(image=wrong_img, highlightthickness=0, command=change_word)
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)

wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)

change_word()

window.mainloop()
