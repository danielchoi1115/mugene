from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, status
from app import crud, exceptions, schemas, models
from app.api import deps
from app.schemas.workspace import WorkspaceCreate
from sqlalchemy.orm import Session
router = APIRouter()

# 3


@router.get("/", status_code=status.HTTP_200_OK, response_model=schemas.WorkspaceOut)
def get_workspace(db: Session = Depends(deps.get_db)) -> dict:
    """
    Root Get
    """
    workspace = crud.workspace.get(db=db, id=5)
    return workspace


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

@router.put("/{workspace_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.WorkspaceOut)
def update_workspace(
    workspace_uuid: str, 
    workspace_in: schemas.WorkspaceUpdate,
    db: Session = Depends(deps.get_db)
) -> models.Workspace:

    db_obj = crud.workspace.get_by_uuid(db=db, uuid=workspace_uuid)
    if not db_obj:
        raise exceptions.WorkspaceNotFoundException
    workspace = crud.workspace.update(db=db, db_obj=db_obj, obj_in=workspace_in)

    return workspace


@router.get("/{workspace_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.WorkspaceOut)
def get_one_workspace(
    workspace_uuid: str, 
    db: Session = Depends(deps.get_db)
) -> models.Workspace:

    workspace = crud.workspace.get_by_uuid(db=db, uuid=workspace_uuid)
    
    return workspace

