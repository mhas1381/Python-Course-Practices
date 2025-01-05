from flask import Flask,render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    # put application's code here
    current_year = datetime.now().year
    return render_template("index.html", current_year = current_year)

@app.route('/<string:name>')
def name_page(name):
    gender = requests.get(url=f"https://api.genderize.io/?name={name}").json()["gender"]
    age = requests.get(url=f'https://api.agify.io/?name={name}').json()["age"]
    
    return render_template("person_info.html" , name = name,gender = gender , age = age )

@app.route('/blog')
def blog():
    all_posts = requests.get(url = "https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog_post.html" , posts = all_posts)

if __name__ == '__main__':
    app.run(debug = True)
