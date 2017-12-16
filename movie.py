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


# Actor URL Paths
@app.route('/actors')
def show_all_actors():
    actors = Actor.query.all()
    return render_template('actor-all.html', actors=actors)


@app.route('/actor/add', methods=['GET', 'POST'])
def add_actors():
    if request.method == 'GET':
        return render_template('actor-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']

        # insert the data into the database
        actor = Actor(name=name, age=age, gender=gender)
        db.session.add(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))


@app.route('/api/actor/add', methods=['POST'])
def add_ajax_artists():
    # get data from the form
    name = request.form['name']
    about = request.form['age']
    gender = request.form['gender']

    # insert the data into the database
    actor = Actor(name=name, age=age, gender=gender)
    db.session.add(actor)
    db.session.commit()
    # flash message type: success, info, warning, and danger from bootstrap
    flash('Actor Inserted', 'success')
    return jsonify({"id": str(actor.id), "name": actor.name})


@app.route('/actor/edit/<int:id>', methods=['GET', 'POST'])
def edit_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actor-edit.html', actor=actor)
    if request.method == 'POST':
        # update data based on the form data
        actor.name = request.form['name']
        actor.age = request.form['age']
        actor.gender = request.form['gender']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_actors'))


@app.route('/actor/delete/<int:id>', methods=['GET', 'POST'])
def delete_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actor-delete.html', actor=actor)
    if request.method == 'POST':
        db.session.delete(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))


@app.route('/api/actor/<int:id>', methods=['DELETE'])
def delete_ajax_actor(id):
    actor = Actor.query.get_or_404(id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({"id": str(actor.id), "name": actor.name})


# Movie URL Paths
@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)


@app.route('/movie/add', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        actors = Actor.query.all()
        return render_template('movie-add.html', actors=actors)
    if request.method == 'POST':
        # get data from the form
        title = request.form['title']
        year = request.form['year']
        description = request.form['description']
        actor_name = request.form['actor']
        actor = Actor.query.filter_by(name=actor_name).first()
        movie = Movie(title=title, year=year, description=description, actor=actor)

        # insert the data into the database
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movie/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    actor = Actor.query.all()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie, actor=actor)
    if request.method == 'POST':
        # update data based on the form data
        movie.title = request.form['title']
        movie.year = request.form['year']
        movie.description = request.form['description']
        actor_name = request.form['actor']
        actor = Actor.query.filter_by(name=actor_name).first()
        movie.actor = actor
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movie/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    actor = Actor.query.all()
    if request.method == 'GET':
        return render_template('movie-delete.html', movie=movie, actor=actor)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/api/movie/<int:id>', methods=['DELETE'])
def delete_ajax_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"id": str(movie.id), "name": movie.name})


@app.route('/members')
def about():
    return render_template('members.html')
