
from app import core
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status
from app import exceptions
from app.api import deps
from app.core.auth import create_access_token, create_refresh_token
from sqlalchemy.orm.session import Session
router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_tokens(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> dict:
    """_summary_

    Args:
        -

    Raises:
        exceptions.user.IncorrectLoginException: When login data is wrong

    Returns:
        dict: contains access token, refresh token, and token type
    """
    user = core.auth.authenticate(
        db=db,
        email=form_data.username, 
        password=form_data.password
    )  # 2
    if not user:
        raise exceptions.user.IncorrectLoginException  # 3

    return {
        "access_token": create_access_token(sub=user.email),  # 4
        "refresh_token": create_refresh_token(sub=user.email),
        "token_type": "bearer"
    }
