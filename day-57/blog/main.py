from flask import Flask, render_template
import requests

app = Flask(__name__)

all_posts = requests.get(url="https://api.npoint.io/1c96492931c6a5a235bd").json()

@app.route('/')
def home():
    return render_template("index.html" , posts = all_posts)

@app.route('/blog/<int:id>')
def blog_single_post(id):
    post = all_posts[id]
    return render_template("post.html" , post = post )

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
if __name__ == "__main__":
    app.run(debug=True)
