from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from ..models import Base

DATABASE_URL = 'sqlite:///database.sqlite'

engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
Session = scoped_session(sessionmaker(bind=engine))

@contextmanager
def get_db():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
