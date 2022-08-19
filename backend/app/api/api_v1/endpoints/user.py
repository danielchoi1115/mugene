
from typing import List
from fastapi import APIRouter, Depends, status
from app.schemas.user import UserCreate
from app import schemas
from app import exceptions
from app import crud
from app import schemas
from app.api import deps
router = APIRouter()

# 3


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.InsertResponse | schemas.InsertResponseError)
def signup_user(user_posted: UserCreate) -> dict:
    """
    Root Get
    """

    user = crud.user.get_by_email(user_posted.email)
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
