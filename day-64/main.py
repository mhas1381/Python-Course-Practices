from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


class EditMovieForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route("/")
def home():
    movies = db.session.execute(
        db.select(Movie).order_by(Movie.ranking)).scalars()
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:id>", methods=['POST', 'GET'])
def edit_movie(id):
    movie = db.get_or_404(Movie, id)
    form = EditMovieForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete/<int:id>", methods=['POST', 'GET'])
def delete_movie(id):
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add")
def add_movie():
    form = AddMovieForm()
    return render_template("add.html" , form = form)


if __name__ == '__main__':
    app.run(debug=True)
