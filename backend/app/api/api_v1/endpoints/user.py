from typing import List
from fastapi import APIRouter
from app.schemas.dbref import RefUser
from app.schemas.user import UserPost
from app.crud.crud_user import CRUDUser
router = APIRouter()

# 3


@router.get("/", status_code=200)
def getUser() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@router.post("/", status_code=202)
def createUser(user: UserPost) -> dict:
    """
    Root Get
    """
    
    insertResert = CRUDUser.create(user)

    return insertResert
