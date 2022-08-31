from typing import Generator, Optional
from pymongo.client_session import ClientSession
from fastapi import Depends, HTTPException, status, Request
from jose import jwt, JWTError
from pydantic import BaseModel
from app import crud
from app import exceptions
from app.db.init_client import client
from app.core.auth import oauth2_scheme
from app.core.config import settings
from app.crud.projections.user import UserFullProjection
from app.exceptions import CredentialException
from app import models
from app.db import session
from sqlalchemy.orm import Session
from fastapi.security.utils import get_authorization_scheme_param
class TokenData(BaseModel):
    username: Optional[str] = None


# def get_session() -> Generator:
#     session = client.start_session()
#     try:
#         yield session
#     finally:
#         session.end_session()

def get_db() -> Generator:
    try:
        db = session.SessionLocal()
        yield db
    finally:
        db.close()

async def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> models.User | None:

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

    user = crud.user.get_by_email(db=db, email=username)

    if user is None:
        raise CredentialException
    return user

async def workspace_scheme(request: Request) -> Optional[str]:
    workspace_token: str = request.headers.get("Workspace")
    scheme, param = get_authorization_scheme_param(workspace_token)
    if not workspace_token or scheme.lower() != "uuid":
        raise exceptions.NoWorkspaceException
    return param

async def get_current_workspace(
    db: Session = Depends(get_db),
    # uuid: str = Depends(workspace_scheme)
) -> models.Workspace | None:
    uuid = b'FUj776jLTQSUb78VtJHK8A'
    workspace = crud.workspace.get_by_uuid(db, uuid)

    if workspace is None:
        raise exceptions.NoWorkspaceException
    return workspace
