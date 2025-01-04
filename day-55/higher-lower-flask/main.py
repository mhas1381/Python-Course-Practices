from flask import Flask
from random import randint
app = Flask(__name__)

@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'

number = randint(0,9)
print(number)
@app.route("/<int:gussed>")
def guess(gussed):
    if gussed < number:
        return '<h1 style="color:red">Too low, Try Again!</h1>\
            <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img>'
    elif gussed == number:
        return '<h1 style="color:green">You found me</h1>\
            <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img>'
    else:
        return '<h1 style="color:purple">Too high, Try Again!</h1>\
            <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></img>'

            

if __name__ == "__main__":
    app.run(debug=True)