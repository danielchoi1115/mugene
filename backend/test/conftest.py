from asyncio import get_event_loop
import pytest
from typing import Generator
from fastapi import FastAPI
from asgi_lifespan import LifespanManager
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from asyncpg.pool import Pool
from httpx import AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.schemas import UserInDB
from app import crud
from app.core import Settings, get_settings

def settings_override():
    return Settings(USERDB_URL="mysql+mysqlconnector://root:secret@localhost:3306/test_db")

@pytest.fixture
def app() -> FastAPI:
    from app.main import get_application  # local import for testing purpose

    app = get_application(settings=settings_override())
    app.dependency_overrides[get_settings] = settings_override
    
    return app

@pytest.fixture
async def test_client(app: FastAPI):
    async with AsyncClient(app=app, base_url='http://localhost:8000') as client:
        yield client
        
def create_session() -> Session:
    from app.db import session

    return session.SessionLocal()

@pytest.fixture
def test_db() -> Session:
    """ get db session generator

    Yields:
        Generator: yields `session` Object
    """
    # try:
    db = create_session()
    return db
    # finally:
    #     db.close()


@pytest.fixture
def test_user(test_db: Session) -> UserInDB:
    # user_in = UserCreate(
    #     email="test@example.com",
    #     first_name="Test",
    #     last_name="User",
    #     organization_code="Test Ltd",
    #     account_level=1,
    #     password="123"
    # )
    email="test@example.com"
    user_obj = crud.user.get_by_email(db=test_db, email=email)
    return user_obj

@pytest.fixture
def token(test_user: UserInDB):
    from app.core.auth import create_access_token
    access_token = create_access_token(sub=test_user.email)
    return access_token

@pytest.fixture
def authorized_client(
    app: FastAPI,
    test_client: AsyncClient, 
    token: str,
) -> AsyncClient:
    test_client.headers = {
        "Authorization": f"Bearer {token}",
        **test_client.headers,
    }
    return test_client