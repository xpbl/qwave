from datetime import datetime, timezone
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

    id =            Column(Integer,  primary_key = True,  autoincrement = True)
    username =      Column(String(255), nullable = False, unique = True, index = True)
    created_at =    Column(DateTime,    nullable = False, default = datetime.now(timezone.utc))
    password_hash = Column(String(255), nullable = False)

    tracks =    relationship("Track",    back_populates = "added_by", cascade = "all, delete-orphan")
    sessions =  relationship("Session",  back_populates = "user",     cascade = "all, delete-orphan")
    playlists = relationship("Playlist", back_populates = "owner",    cascade = "all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
    
class Session(Base):
    __tablename__ = "sessions"
    
    id =         Column(Integer, primary_key = True,  autoincrement = True)
    token =      Column(String(36), nullable = False, unique = True, index = True) # UUID
    created_at = Column(DateTime,   nullable = False, default = datetime.now(timezone.utc))
    expires_at = Column(DateTime,   nullable = False)
    user_id =    Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
    
    user = relationship("User", back_populates = "sessions")
    
    def __repr__(self):
        return f"<Session(id={self.id}, user_id={self.user_id}, expires_at={self.expires_at})>"

class Artist(Base):
    __tablename__ = "artists"

    id =   Column(Integer,  primary_key = True, autoincrement = True)
    name = Column(String(255), nullable = False, unique = True, index = True)
    
    tracks = relationship("Track", back_populates = "artists", secondary = track_artists)
    albums = relationship("Album", back_populates="album_artist")
    
    def __repr__(self):
        return f"<Artist(id={self.id}, name='{self.name}')>"
    
class Album(Base):
    __tablename__ = "albums"
    
    id =              Column(Integer,  primary_key = True, autoincrement = True)
    title =           Column(String(255), nullable = False, index = True)
    release_date =    Column(DateTime,    nullable = True)
    album_artist_id = Column(Integer, ForeignKey("artists.id", ondelete = "SET NULL"), nullable = True)
    
    album_artist = relationship("Artist", back_populates = "albums")
    tracks =       relationship("Track",  back_populates = "album", cascade = "all, delete-orphan")
    
    def __repr__(self):
        return f"<Album(id={self.id}, title='{self.title}')>"

class Track(Base):
    __tablename__ = "tracks"
    
    id =               Column(Integer,  primary_key = True, autoincrement = True)
    title =            Column(String(255), nullable = False, index = True)
    lyrics =           Column(Text,        nullable = True)
    duration =         Column(Float,       nullable = False) # seconds
    file_path =        Column(String(512), nullable = False) # original path
    opus_path =        Column(String(512), nullable = False) # usable path
    added_date =       Column(DateTime,    nullable = False, default = datetime.now(timezone.utc))
    track_number =     Column(Integer,     nullable = True)
    needs_review =     Column(Boolean,     nullable = False, default = False)
    cover_art_path =   Column(String(512), nullable = True) # keep null
    added_by_user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
    album_id =         Column(Integer, ForeignKey("albums.id", ondelete = "SET NULL"), nullable = True)
    
    jobs =     relationship("Job",    back_populates = "track", cascade = "all, delete-orphan")
    album =    relationship("Album",  back_populates = "tracks")
    genres =   relationship("Genre",  back_populates = "tracks", secondary = track_genres)
    artists =  relationship("Artist", back_populates = "tracks", secondary = track_artists)
    added_by = relationship("User",   back_populates = "tracks")
    
    def __repr__(self):
        return f"<Track(id={self.id}, title='{self.title}', duration={self.duration})>"

class Genre(Base):
    __tablename__ = "genres"
    
    id =     Column(Integer,  primary_key = True, autoincrement = True)
    name =   Column(String(100), nullable = False, unique = True, index = True)
    tracks = relationship("Track", secondary = track_genres, back_populates = "genres")
    
    def __repr__(self):
        return f"<Genre(id={self.id}, name='{self.name}')>"

class Playlist(Base):
    __tablename__ = "playlists"
    
    id =         Column(Integer,  primary_key = True, autoincrement = True)
    name =       Column(String(255), nullable = False)
    is_public =  Column(Boolean,     nullable = False, default = False)
    created_at = Column(DateTime,    nullable = False, default = datetime.now(timezone.utc))
    user_id =    Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
    
    owner =  relationship("User",  back_populates = "playlists")
    tracks = relationship("Track", back_populates = None, secondary = playlist_tracks)
    
    def __repr__(self):
        return f"<Playlist(id={self.id}, name='{self.name}', is_public={self.is_public})>"

class Job(Base): # ooooooo spooopy
    __tablename__ = "jobs"
    
    id =            Column(Integer, primary_key = True, autoincrement = True)
    type =          Column(String(50), nullable = False) # "transcode", "fingerprint", etc
    status =        Column(String(50), nullable = False, default = "pending") # "pending", "running", "complete", "failed"
    created_at =    Column(DateTime,   nullable = False, default = datetime.now(timezone.utc))
    started_at =    Column(DateTime,   nullable = True)
    completed_at =  Column(DateTime,   nullable = True)
    error_message = Column(Text,       nullable = True)
    track_id =      Column(Integer, ForeignKey("tracks.id", ondelete = "CASCADE"))
    track =         relationship("Track", back_populates = "jobs")
    
    def __repr__(self):
        return f"<Job(id={self.id}, type='{self.type}', status='{self.status}')>"