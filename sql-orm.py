from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "artist" table
class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "album"
    album_id = column(Integer, primary_key=True)
    Title = Column(String)
    artist_id = Column(Integer, ForeignKey("Artist.artist_id"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    track_id = Column(integer, primary_key=True)
    Name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.album_id"))
    MediaTypeId = Column(Integer, ForeignKey("Album.album_id"))
    GenreId = Column(Integer, primary_key=False)
    composer = Column(String)
    mi


# instead of connecting to the database directly directly, we will ask for a session
# create a new instance of sessionmaker,  then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)