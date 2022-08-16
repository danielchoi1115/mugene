from typing import Optional, MutableMapping, List, Union
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from app.core.config import settings
from app.core.security import verify_password
from app import crud

from pydantic import EmailStr

from app.crud.projections.user import UserAuthProjection
from app.schemas.user import UserInDB

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/user/token")
print(oauth2_scheme)


def authenticate(
    *,
    email: EmailStr,
    password: str
) -> Optional[UserInDB]:
    user = crud.user.get_by_email(email, UserAuthProjection())
    if not user:
        return None
    if not verify_password(password, user.hashed_password):  # 1
        return None
    return user


def create_access_token(*, sub: str) -> str:  # 2
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),  # 3
        sub=sub,
    )


def _create_token(
    token_type: str,
    lifetime: timedelta,
    sub: str,
) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire  # 4
    payload["iat"] = datetime.utcnow()  # 5
    payload["sub"] = str(sub)  # 6

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)  # 8
