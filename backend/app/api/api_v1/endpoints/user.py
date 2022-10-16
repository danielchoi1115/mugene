
from fastapi import APIRouter, Depends, status
from app.schemas.user import UserCreate
from app import schemas
from app import exceptions
from app import crud
from app import schemas
from app import models
from app.api import deps
from sqlalchemy.orm import Session
router = APIRouter()

# 3

# response_model=schemas.InsertResponse | schemas.InsertResponseError
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def signup_user(
    user_in: UserCreate, 
    db: Session = Depends(deps.get_db)
) -> models.User:
    """
    Root Get
    """

    user = crud.user.get_by_email(db=db, email=user_in.email)
    if user:
        raise exceptions.user.UserExistException()

    user = crud.user.create(db=db, obj_in=user_in)

    return user


@router.get("/me", response_model=schemas.UserOut)
def read_users_me(
    current_user: models.User = Depends(deps.get_current_user)
):
    """
    Fetch the current logged in user.
    """

    user = current_user
    return user

@router.get("/{user_uuid}", response_model=schemas.UserOut)
def read_users_me(
    user_uuid: str, 
    db: Session = Depends(deps.get_db)
):
    """
    Fetch the current logged in user.
    """

    user = crud.user.get_by_uuid(db=db, uuid=user_uuid)
    if not user:
        raise exceptions.user.UserNotFoundException
    return user
