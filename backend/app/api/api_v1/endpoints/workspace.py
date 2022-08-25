from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, status
from app import crud, exceptions, schemas
from app.schemas.dbref import RefWorkspace
from pymongo.client_session import ClientSession
from app.api import deps
from app.schemas.member import Member
from app.schemas.pyobjectid import PyObjectId
from app.schemas.workspace import WorkspaceCreate
from sqlalchemy.orm import Session
from app.crud.crud_workspace import CRUDWorkspace
from app import models
router = APIRouter()

# 3


@router.get("/", status_code=200)
def get_workspace() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.WorkspaceOut)
def create_workspace(
    workspace_in: WorkspaceCreate,
    db: Session = Depends(deps.get_db),
    user_in: models.User = Depends(deps.get_current_user)
) -> models.User:
    """
    Root Get
    """
    user = crud.workspace.create(db=db, user_in=user_in, obj_in=workspace_in)

    return user

@router.put("/members", status_code=status.HTTP_200_OK)
def update_members(
    workspace_id: PyObjectId,
    members: List[Member],
    session: ClientSession = Depends(deps.get_db)
) -> schemas.UpdateResponse:
    
    update_result = crud.workspace.add_members(
        workspace_id=workspace_id,
        members=members,
        session=session
    )
    return update_result
    
@router.put("/members/{memberId}", status_code=status.HTTP_201_CREATED)
def create_workspac(
    list: WorkspaceCreate,
    session: ClientSession = Depends(deps.get_db)
) -> schemas.UpdateResponse:
    ... 