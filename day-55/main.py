from flask import Flask

app  = Flask(__name__)

@app.route("/<string:name>/<int:age>/")
def hello(name , age):
    return f"<h1>Hello {name},you are {age} years old.</h1>"


def bold(function):
    def wrapper():
        returned_value = f"<b>{function()}</b>"

        return returned_value
     
    return wrapper

def italic(function):
    def wrapper():
        returned_value = f"<em>{function()}</em>"

        return returned_value
     
    return wrapper

def underline(function):
    def wrapper():
        returned_value = f"<u>{function()}</u>"      
     
        return returned_value
     
    return wrapper

@app.route("/")
@bold
@italic
@underline
def salam():
    return "Salam"

if __name__ == "__main__":
    app.run(debug=True)