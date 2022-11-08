from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core import settings

engine = create_engine(
    settings.USERDB_URL, 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 