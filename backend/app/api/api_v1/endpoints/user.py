
from typing import List
from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse, UserCreate, UserResponseError
from app import exceptions
from app import crud
from app import core
from app import schemas
from app.api import deps
from fastapi.security import OAuth2PasswordRequestForm

from app.core.auth import create_access_token

router = APIRouter()

# 3


@router.get("/", status_code=200)
def get_user() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@router.post("/new", status_code=202, response_model=UserResponse | UserResponseError)
def signup_user(user_posted: UserCreate) -> dict:
    """
    Root Get
    """

    user = crud.user.get_by_email(email=user_posted.email)
    if user:
        raise exceptions.user.UserExistException()

    user = crud.user.create(user_posted)

    return user


@router.get("/me", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(deps.get_current_user)):
    """
    Fetch the current logged in user.
    """

    user = current_user
    return user


@router.post("/token", status_code=202)
def get_user_token(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    """
    Root Get
    """
    user = core.auth.authenticate(email=form_data.username, password=form_data.password)  # 2
    if not user:
        raise exceptions.user.IncorrectLoginException  # 3

    return {
        "access_token": create_access_token(sub=user.email),  # 4
        "token_type": "bearer",
    }
