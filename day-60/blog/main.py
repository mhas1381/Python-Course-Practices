from flask import Flask, render_template , request
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
    
@app.route('/form-entry', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
    return render_template("has_sent.html", name = name, email = email, phone = phone, message = message)
    
if __name__ == "__main__":
    app.run(debug=True)
