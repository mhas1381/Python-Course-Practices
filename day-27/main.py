from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(height=500 , width=500)
window.config(padx = 20 , pady = 20)

# Label
first_label = Label(text = "Salam" , font=("Arial" , 24))
first_label.grid(row = 0 , column = 0)

# Button
def button_clicked():
    first_label['text'] = input.get()

button = Button(text = "click me" , command = button_clicked)
button.grid(row = 1 , column = 1)

button2 = Button(text = "new")
button2.grid(row = 0 , column =2)
# Entry
input = Entry(width=10)
input.grid(row = 2 , column = 3)



window.mainloop()
