from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from typing import List, Optional
from .models import Track, Tag, track_tags

def get_all_tracks(db: Session) -> List[dict]:
    """Get all tracks with their tags as arrays"""
    query = select(
        Track,
        func.array_agg(Tag.name).label('tags')
    ).outerjoin(track_tags).outerjoin(Tag).group_by(Track.id)
    
    result = db.execute(query).all()
    return [
        {
            **track.__dict__,
            'tags': tags if tags[0] is not None else []
        }
        for track, tags in result
    ]

def get_all_tags(db: Session) -> List[Tag]:
    """Get all tags"""
    return db.execute(select(Tag)).scalars().all()

def create_tag(db: Session, name: str) -> Tag:
    """Create a new tag"""
    tag = Tag(name=name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def update_tag(db: Session, tag_id: int, new_name: str) -> Optional[Tag]:
    """Update tag name"""
    tag = db.get(Tag, tag_id)
    if tag:
        tag.name = new_name
        db.commit()
        db.refresh(tag)
    return tag

def delete_tag(db: Session, tag_id: int) -> bool:
    """Delete a tag"""
    result = db.execute(delete(Tag).where(Tag.id == tag_id))
    db.commit()
    return result.rowcount > 0

def add_tags_to_track(db: Session, track_id: int, tag_ids: List[int]) -> bool:
    """Add multiple tags to a track"""
    track = db.get(Track, track_id)
    if not track:
        return False
    
    for tag_id in tag_ids:
        db.execute(
            track_tags.insert().values(
                track_id=track_id,
                tag_id=tag_id
            )
        )
    db.commit()
    return True

def remove_tags_from_track(db: Session, track_id: int, tag_ids: List[int]) -> bool:
    """Remove multiple tags from a track"""
    result = db.execute(
        delete(track_tags).where(
            track_tags.c.track_id == track_id,
            track_tags.c.tag_id.in_(tag_ids)
        )
    )
    db.commit()
    return result.rowcount > 0

def create_track_if_not_exists(db: Session, youtube_id: str, title: str, artist: str) -> Track:
    """Create a track if it doesn't exist"""
    track = db.query(Track).filter(Track.youtube_id == youtube_id).first()
    exists = track is not None
    
    if not exists:
        track = Track(youtube_id=youtube_id, title=title, artist=artist)
        db.add(track)
    
    db.commit()
    db.refresh(track)

    return (track, not exists)
