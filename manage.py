from flask_script import Manager
from movie import app, db, Actor, Movie

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    actor1 = Actor(name='Robert Downey Jr.', age='52', gender='Male')
    actor2 = Actor(name='Scarlett Johansson', age='33', gender='Female' )
    actor3 = Actor(name='Christian Bale', age='43', gender='Male' )
    movie1 = Movie(title='Iron Man', year="2008", description="Man made of iron", actor=actor1)
    movie2 = Movie(title='The Avengers', year="2012", description="Avengers save the world", actor=actor2)
    movie3 = Movie(title='The Dark Knight', year="2008", description="Batman vs Joker", actor=actor3)
    db.session.add(actor1)
    db.session.add(actor2)
    db.session.add(actor3)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
