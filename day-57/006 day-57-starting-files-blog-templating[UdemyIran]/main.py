from flask import Flask, render_template
import requests

app = Flask(__name__)

all_posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/')
def home():
    return render_template("index.html" , posts = all_posts)

@app.route('/blog/<int:id>')
def blog_single_post(id):
    post = all_posts[id]
    return render_template("post.html" , post = post )

if __name__ == "__main__":
    app.run(debug=True)
