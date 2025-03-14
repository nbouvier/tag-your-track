import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from .models import Base

DATABASE_NAME = "database.sqlite"
DATABASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', DATABASE_NAME))
DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

print(f"Using database at: {DATABASE_PATH}")
if not os.path.exists(DATABASE_PATH):
    raise FileNotFoundError(f"Database file not found at {DATABASE_PATH}")

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
