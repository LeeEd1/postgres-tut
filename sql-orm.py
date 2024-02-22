from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    Title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    Name = Column(String)
    album_id = Column(Integer, ForeignKey("album.album_id"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#  print(artist.artist_id, artist.name, sep=" | ")

# Query 2 - select only the "name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.name)

# query 3 - select only "queen" from the "artist" table
# Artist = session.query(Artist).filter_by(name="Queen").first()
# print(Artist.artist_id, Artist.name, sep="  |  ")

# query 4 - select only "artistid" #51 from the "artist" table
Artist = session.query(Artist).filter_by(artist_id=51).first()
print(Artist.artist_id, Artist.name, sep="  |  ")

# query 5 - select only the albums with "artistid" # 51 on the "album" table
albums = session.query(Album).filter_by(artist_id=51)