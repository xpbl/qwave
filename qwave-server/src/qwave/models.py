from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, Text, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# ASSOCIATION TABLES
track_artists = Table(
    "track_artists",
    Base.metadata,
    Column("track_id", Integer, ForeignKey("tracks.id", ondelete = "CASCADE"), primary_key = True),
    Column("artist_id", Integer, ForeignKey("artists.id", ondelete = "CASCADE"), primary_key = True),
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
    Column("track_id", Integer, ForeignKey("tracks.id", ondelete = "CASCADE"), primary_key = True),
    Column("position", Integer, nullable = False)
)

class User(Base):
    __tablename__ = "users"

    def __repr__(self):
        return f"{'test'}"