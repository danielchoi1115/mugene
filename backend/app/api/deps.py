from typing import Generator, Optional
from pymongo.client_session import ClientSession
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import BaseModel
from app import crud

from app.core.auth import oauth2_scheme
from app.core.config import settings
from app.crud.projections.user import UserFullProjection
from app.exceptions import CredentialException
from app.schemas.user import User


class TokenData(BaseModel):
    username: Optional[str] = None


# def get_session() -> Generator:
#     session = client.start_session()
#     try:
#         yield session
#     finally:
#         session.end_session()


async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> User:

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")
        if username is None:
            raise CredentialException
        token_data = TokenData(username=username)

    except JWTError:
        raise CredentialException

    user = crud.user.get_by_email(
        email=username,
        projection=UserFullProjection
    )

    if user is None:
        raise CredentialException
    return user
