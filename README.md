# MISY350-Project
## Group Project

###### DESCRIPTION:
  We are creating a Movie database for our web application which will have a list a list of actors who have starred in many movies

###### DATABASE:
  Two tables: Movies and Actors
  One-to-Many relationship where Actor has many Movies
  -Movies Table Columns: MovieID, ActorID, Title, Year, Lead Actor, Description
  -Actors Table Columns: ActorID, Name, Age, Gender
  ActorID will be PK in Actors

  ## Setup Instructions:

Make sure to use Python version 2.7.x.

Install `virtualenv` if needed.

If you do not have a virtual environment yet on the project folder, set it up with:

    $ virtualenv venv

Then activate the virtual environment

    $ source venv/bin/activate

Install packages

    $ pip install -r requirements.txt

To initialize the database:

    $ python manage.py deploy

To run the development server (use `-d` to enable debugger and reloader):

    $ python manage.py runserver -d

# **Tables:**
### Actors

Number | Name | Age | Gender
------------ | ------------- | ------------ | ------------ |
1 | Robert Downey Jr. | 52 | Male
2 | Scarlett Johansson | 33 | Female
3 | Christian Bale | 43 | Male

### Movies

Number | Title | Year | Actor | Description
------------ | ------------- | ------------ | ------------ | ------------ |
1 | Iron Man | 52 | Robert Downey Jr. | Man made of iron
2 | The Avengers | 33 | Scarlett Johansson | Avengers save the world
3 | The Dark Knight | 43 | Christian Bale | Batman vs Joker
