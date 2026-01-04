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
    __tablename__ = "sessions"
    
    id =         Column(Integer)
    user_id =    Column(Integer)
    token =      Column(String(36))
    created_at = Column(DateTime)
    expires_at = Column(DateTime)
    
    user = relationship("User", back_populates = "sessions")
    
    def __repr__(self):
        return f""

class Artist(Base):
    __tablename__ = "artists"

    id =   Column(Integer)
    name = Column(String(255))
    
    tracks = relationship("Track", secondary = track_artists, back_populates = "artists")
    albums = relationship("Album", back_populates="album_artist")
    
    def __repr__(self):
        return f""
    
class Album(Base):
    __tablename__ = "albums"
    
    id =              Column(Integer)
    title =           Column(String(255))
    release_date =    Column(DateTime)
    album_artist_id = Column(Integer)
    
    album_artist = relationship("Artist")
    tracks =       relationship("Track")
    
    def __repr__(self):
        return f""

class Track(Base):
    __tablename__ = "tracks"
    
    id =               Column(Integer,  primary_key = True)
    title =            Column(String(255), nullable = False)
    lyrics =           Column(Text,        nullable = True)
    duration =         Column(Integer,     nullable = False) # seconds
    album_id =         Column(Integer,     nullable = True)
    file_path =        Column(String(512), nullable = False) # original path
    opus_path =        Column(String(512), nullable = False) # usable path
    added_date =       Column(DateTime,    nullable = False)
    track_number =     Column(Integer,     nullable = True)
    needs_review =     Column(Boolean,     nullable = False)
    cover_art_path =   Column(String(512), nullable = True) # keep null
    added_by_user_id = Column(Integer,     nullable = False)
    
    jobs =     relationship("Job")
    album =    relationship("Album")
    genres =   relationship("Genre")
    artists =  relationship("Artist")
    added_by = relationship("User")
    
    def __repr__(self):
        return f""

class Genre(Base):
    __tablename__ = "genres"
    
    id =     Column(Integer)
    name =   Column(String(100))
    tracks = relationship("Track")
    
    def __repr__(self):
        return f""

class Playlist(Base):
    __tablename__ = "playlists"
    
    id =         Column(Integer)
    name =       Column(String(255))
    user_id =    Column(Integer)
    is_public =  Column(Boolean)
    created_at = Column(DateTime)
    
    owner =  relationship("User")
    tracks = relationship("Track")
    
    def __repr__(self):
        return f""

class Job(Base): # ooooooo spooopy
    __tablename__ = "jobs"
    
    id =            Column(Integer)
    type =          Column(String(50)) # "transcode", "fingerprint", etc
    status =        Column(String(50)) # "pending", "running", "complete", "failed"
    track_id =      Column(Integer)
    created_at =    Column(DateTime)
    started_at =    Column(DateTime)
    completed_at =  Column(DateTime)
    error_message = Column(Text)
    track =         relationship("Track")
    
    def __repr__(self):
        return f""