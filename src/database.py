import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from alembic import command
from alembic.config import Config
from .models import Base

DATABASE_NAME = "database.sqlite"
DATABASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', DATABASE_NAME))
DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

def run_migrations():
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', 'alembic')
    alembic_cfg.set_main_option('sqlalchemy.url', DATABASE_URL)
    command.upgrade(alembic_cfg, 'head')

def init_database():
    """Initialize the database, create tables and run migrations"""
    run_migrations()

print(f"Using database at: {DATABASE_PATH}")

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
