from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os  # Ensure os is imported for environment variable access


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./bucket_files.sqlite3")

# check_same_thread=False needed because SQLite + background thread + FastAPI
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """FastAPI dependency — yields a DB session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()