from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# Colors and Fonts
BG_COLOR = "#fef6e4"
ACCENT_COLOR = "#f582ae"
BUTTON_COLOR = "#ff99c8"
TEXT_COLOR = "#4a4e69"
FONT_NAME = "Calibri"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    letters_password = [choice(letters) for _ in range(randint(8, 10))]
    symbols_pass = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_pass = [choice(numbers) for _ in range(randint(2, 4))]

    generated_password = letters_password + symbols_pass + numbers_pass
    shuffle(generated_password)

    result = ''.join(generated_password)
    password_entry.delete(0, END)
    password_entry.insert(0, result)
    pyperclip.copy(result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please fill in all the fields.")
    else:
        try:
            with open('data.json', "r") as datafile:
                # Reading old data
                data = json.load(datafile)
        except FileNotFoundError:
            with open('data.json', "w") as datafile:
                json.dump(new_data, datafile, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search Password ------------------------------- #
def find_password():
    try:
        with open('data.json', 'r') as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showerror(title = "Oops" , message = "No Data file found")
        return
    email = email_entry.get()
    website = website_entry.get()

    try:
        finded_password = data[website]['password']
        messagebox.showinfo(title=website,
                        message=f"Email: {email}\nPassword: {finded_password}\nPassword copied to clipboard.")
        pyperclip.copy(finded_password)
    except KeyError:
        messagebox.showwarning(title="Oops" , message="You don't have saved this site.")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.resizable(0, 0)

# Icon
icon = PhotoImage(file='icon.png')
window.iconphoto(False, icon)

# Logo
canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
pin_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=pin_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=(FONT_NAME, 12, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
website_label.grid(row=1, column=0, pady=5)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
email_label.grid(row=2, column=0, pady=5)

password_label = Label(text="Password:", font=(FONT_NAME, 12, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
password_label.grid(row=3, column=0, pady=5)

# Entries
website_entry = Entry(width=24, font=(FONT_NAME, 12))
website_entry.grid(row=1, column=1, pady=5)
website_entry.focus()

email_entry = Entry(width=38, font=(FONT_NAME, 12))
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "mhas.software@gmail.com")

password_entry = Entry(width=24, font=(FONT_NAME, 12))
password_entry.grid(row=3, column=1, pady=5)

# Buttons
search_btn = Button(text="Search", command=find_password, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                    font=(FONT_NAME, 10, "bold"), highlightthickness=0)
search_btn.grid(row=1, column=2, pady=5, sticky="wnes")

generate_password_btn = Button(text="Generate Password", command=generate_password, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                               font=(FONT_NAME, 10, "bold"), highlightthickness=0)
generate_password_btn.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", width=38, command=save, bg=ACCENT_COLOR, fg="white", font=(FONT_NAME, 12, "bold"),
                    highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

# Run UI
window.mainloop()
