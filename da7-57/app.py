from lib2to3.fixes.fix_input import context

from flask import Flask,render_template
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    # put application's code here
    current_year = datetime.now().year
    return render_template("index.html", current_year = current_year)


if __name__ == '__main__':
    app.run(debug = True)
