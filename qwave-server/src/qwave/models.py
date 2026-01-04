import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, Text, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# ASSOCIATION TABLES
track_artists = Table(
    "track_artists",
    Base.metadata,
    Column("track_id",   Integer, ForeignKey("tracks.id",  ondelete = "CASCADE"), primary_key = True),
    Column("artist_id",  Integer, ForeignKey("artists.id", ondelete = "CASCADE"), primary_key = True),
    Column("is_primary", Boolean, default = False, nullable = False)
)

track_genres = Table(
    "track_genres",
    Base.metadata,
    Column("track_id", Integer, ForeignKey("tracks.id", ondelete = "CASCADE"), primary_key = True),
    Column("genre_id", Integer, ForeignKey("genres.id", ondelete = "CASCADE"), primary_key = True)
)

playlist_tracks = Table(
    "playlist_tracks",
    Base.metadata,
    Column("playlist_id", Integer, ForeignKey("playlists.id", ondelete = "CASCADE"), primary_key = True),
    Column("track_id",    Integer, ForeignKey("tracks.id",    ondelete = "CASCADE"), primary_key = True),
    Column("position",    Integer, nullable = False)
)

class User(Base):
    __tablename__ = "users"

    id =            Column(Integer, primary_key = True, autoincrement = True)
    username =      Column(String(255), nullable = False, unique = True, index = True)
    password_hash = Column(String(255), nullable = False)
    created_at =    Column(DateTime,    nullable = False, default = datetime.datetime.now(datetime.timezone.utc))

    sessions =  relationship("Session",  back_populates = "user",     cascade = "all, delete-orphan")
    tracks =    relationship("Track",    back_populates = "added_by", cascade = "all, delete-orphan")
    playlists = relationship("Playlist", back_populates = "owner",    cascade = "all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
    
class Session(Base):
    pass

class Artist(Base):
    pass

class Album(Base):
    pass

class Track(Base):
    pass

class Genre(Base):
    pass

class Playlist(Base):
    pass

class Job(Base): # ooooooo spooopy
    pass