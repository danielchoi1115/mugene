from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, status
from app import crud, exceptions, schemas
from app.schemas.dbref import RefWorkspace
from pymongo.client_session import ClientSession
from app.api import deps
from app.schemas.pyobjectid import PyObjectId
from app.schemas.workspace import WorkspaceCreate
from sqlalchemy.orm import Session
from app.crud.crud_workspace import CRUDWorkspace
from app import models
router = APIRouter()

# 3


@router.get("/", status_code=status.HTTP_200_OK, response_model=schemas.WorkspaceOut)
def get_workspace(db: Session = Depends(deps.get_db)) -> dict:
    """
    Root Get
    """
    workspace = crud.workspace.get(db=db, id=5)
    workspace.workspace_uuid = workspace.workspace_uuid.strip().decode('ascii')
    return workspace
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
    workspace = crud.workspace.create(db=db, user_in=user_in, obj_in=workspace_in)

    return workspace

@router.put("/{workspace_id}", status_code=status.HTTP_200_OK, response_model=schemas.WorkspaceOut)
def update_workspace(
    workspace_id: int, 
    workspace_in: schemas.WorkspaceUpdate,
    db: Session = Depends(deps.get_db)
) -> models.Workspace:
    """
    Root Get
    """
    db_obj = crud.workspace.get(db=db, id=workspace_id)
    workspace = crud.workspace.update(db=db, db_obj=db_obj, obj_in=workspace_in)

    return workspace
