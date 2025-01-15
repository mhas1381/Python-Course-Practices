from flask import Flask, render_template, request, redirect, url_for
import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,sessionmaker
from sqlalchemy import Integer, String, Float
'''
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id = mapped_column(Integer, primary_key=True , autoincrement=True)
    title = mapped_column(String(30), unique=True, nullable=False)
    author = mapped_column(String(30), nullable=False)
    rating = mapped_column(String(30), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    message = request.args.get('message')
    query = sa.select(Book)
    books = db.session.scalars(query).all()
    return render_template("index.html" , books = books , message=message)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")

        if title and author and rating:  # Ensure all fields are filled
            new_book = Book(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return "Please fill in all fields.", 400

    return render_template("add.html")

@app.route("/edit/<int:book_id>" , methods = ["POST", "GET"])
def edit_rating(book_id):
    book = Book.query.get(book_id)
    if request.method == "POST":
        if book:
            new_rating = request.form.get('rating')
            if new_rating:
                book.rating = new_rating  
                db.session.commit() 
    return render_template("edit.html" , book = book)

@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = Book.query.get(book_id)
    if book:
            db.session.delete(book)  
            db.session.commit()
            message = f"Book '{book.title}' deleted successfully."
    else:
        message = "Book not found."
    return redirect(url_for('home', message=message))

if __name__ == "__main__":
    app.run(debug=True)
