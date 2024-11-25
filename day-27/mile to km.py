from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input_mile = Entry(width=15)
input_mile.grid(row=0, column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

label_is_equal = Label(text="is equal to:")
label_is_equal.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


def calculate():
    result_label['text'] = round(round(input_mile.get()) * 1.609, 2)


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
