from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

engine = create_engine(
    settings.USERDB_URL, 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 