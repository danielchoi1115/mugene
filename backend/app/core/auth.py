from typing import Optional, MutableMapping, List, Union
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app import crud
from app import models
from pydantic import EmailStr
from app import schemas
from sqlalchemy.orm import Session
from app.core.config import get_settings, Settings
from app.core.security import verify_password

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]

def oauth2_scheme(
    *,
    settings: Settings = Depends(get_settings)
) -> OAuth2PasswordBearer:
    return OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth")

def authenticate(
    *,
    db: Session,
    email: EmailStr,
    password: str
) -> Optional[schemas.UserInDB]:
    """Method to check email existance and verify password

    Args:
        email (EmailStr): user email
        password (str): password

    Returns:
        User object or None
    """
    user: models.User = crud.user.get_by_email(db=db, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(
    *, 
    sub: str, 
    settings: Settings = Depends(get_settings)
) -> str:  # 2
    """Creates user access token with email

    Args:
        sub (str): user email

    Returns:
        str: access token string
    """
    print('settings.USERDB_URL',settings.USERDB_URL)
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),  # 3
        sub=sub,
    )


def create_refresh_token(
    *, 
    sub: str, 
    settings: Settings = Depends(get_settings)
) -> str:  # 2
    """Creates user refresh token with email

    Args:
        sub (str): user email

    Returns:
        str: refresh token string
    """
    return _create_token(
        token_type="refresh_token",
        lifetime=timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES),  # 3
        sub=sub,
    )


def _create_token(
    token_type: str,
    lifetime: timedelta,
    sub: str,
    settings: Settings = Depends(get_settings)
) -> str:
    """_summary_

    Args:
        token_type (str): token type -> `access_token` or `refresh_token`
        lifetime (timedelta): token lifetime
        sub (str): data

    Returns:
        str: returns token
    """
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire  # 4
    payload["iat"] = datetime.utcnow()  # 5
    payload["sub"] = str(sub)  # 6

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)  # 8
