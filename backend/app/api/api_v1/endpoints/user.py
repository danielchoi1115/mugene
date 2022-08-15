from typing import List
from fastapi import APIRouter
from app.schemas.user import UserResponse, UserPost, UserEmail, UserResponseError
from app.crud.crud_user import CRUDUser
from app import exceptions
from app import crud

router = APIRouter()

# 3


@router.get("/", status_code=200)
def get_user() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@router.post("/new", status_code=202, response_model=UserResponse | UserResponseError,)
def signup_user(user_posted: UserPost) -> dict:
    """
    Root Get
    """

    user = crud.user.get_by_email(UserEmail(email=user_posted.email))
    if user:
        raise exceptions.user.UserExistException

    user = crud.user.create(user_posted)

    return user


@router.post("/", status_code=202)
def create_user(user: UserPost) -> dict:
    """
    Root Get
    """

    return 'insertResert'
