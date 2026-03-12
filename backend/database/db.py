from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# ------------------------------------------------------------------
# Database Configuration
# ------------------------------------------------------------------

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./insightflow.db"   # Default for local development
)


# ------------------------------------------------------------------
# Engine Creation
# ------------------------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)


# ------------------------------------------------------------------
# Session Factory
# ------------------------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ------------------------------------------------------------------
# Base Class for ORM Models
# ------------------------------------------------------------------

Base = declarative_base()


# ------------------------------------------------------------------
# Dependency for FastAPI
# ------------------------------------------------------------------

def get_db():
    """
    Dependency used by FastAPI routes to get DB session
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ------------------------------------------------------------------
# Database Initialization
# ------------------------------------------------------------------

def init_db():
    """
    Create all tables automatically.
    """

    from backend.models.user import User
    from backend.models.dataset import Dataset
    from backend.models.metrics import ModelMetrics

    Base.metadata.create_all(bind=engine)