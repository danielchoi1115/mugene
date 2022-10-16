from typing import Generator, Optional
from fastapi import Depends, Request
from jose import jwt, JWTError
from pydantic import BaseModel
from app import crud
from app import exceptions
from app.core.auth import oauth2_scheme
from app.core.config import settings
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
    # get generator 
    try:
        db = session.SessionLocal()
        yield db
    finally:
        db.close()

async def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> models.User | None:
    # fetch user data from token
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
        raise exceptions.WorkspaceNotFoundException
    return param

async def get_current_workspace(
    db: Session = Depends(get_db),
    # uuid: str = Depends(workspace_scheme)
) -> models.Workspace | None:
    # fetch workspace data from token
    uuid = b'FUj776jLTQSUb78VtJHK8A'
    workspace = crud.workspace.get_by_uuid(db, uuid)

    if workspace is None:
        raise exceptions.WorkspaceNotFoundException
    if workspace.is_active == 0:
        raise exceptions.InactiveWorkspace
    return workspace
