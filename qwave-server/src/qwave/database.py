from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from pathlib import Path
from typing import Generator

from qwave.models import Base
from qwave.config import get_config # TODO

_engine = None
_SessionLocal = None

def init_db(database_url: str):
    global _engine, _SessionLocal
    
    # etc
    
    return _engine