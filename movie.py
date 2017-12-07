import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is the secret key'

# SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# database tables
class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Text)
    gender = db.Column(db.Text)
    movies = db.relationship('Movie', backref='actor', cascade="delete")


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/actors')
def show_all_actors():
    actors = Actor.query.all()
    return render_template('actor-all.html', actors=actors)


@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)


@app.route('/members')
def about():
    return render_template('members.html')
