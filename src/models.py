from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

track_tags = Table(
    'track_tags',
    Base.metadata,
    Column('track_id', Integer, ForeignKey('tracks.id', ondelete='CASCADE')),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE')),
    Column('created_at', DateTime, default=func.now())
)

class Track(Base):
    __tablename__ = 'tracks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artist = Column(String)
    album = Column(String)
    note = Column(String)
    youtube_id = Column(String)
    created_at = Column(DateTime, default=func.now())

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=func.now())
