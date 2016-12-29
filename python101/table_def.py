# creating tables with SQLAlchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# connection string
engine = create_engine('sqlite:///mymusic.db', echo=True)
Base = declarative_base()

# classes based on Base
class Artist(Base):
    """"""
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True) # will auto-increment
    name = Column(String)

class Album(Base):
    """"""
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    publisher = Column(String)
    media_type = Column(String)

    artist_id = Column(Integer, ForeignKey('artists.id')) # uniqely indentifies a row
        # in the 'Artist' table. Lots of different albums can have the same ForignKey,
        # so this is a many-to-one relationship
    artist = relationship('Artist', backref=backref('albums', order_by=id))

# create tables
Base.metadata.create_all(engine)
