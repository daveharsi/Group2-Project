from flask_script import Manager
from movie import app

manager = Manager(app)


@manager.command
def deploy():
    print "Movie Database"


if __name__ == "__main__":
    manager.run()
