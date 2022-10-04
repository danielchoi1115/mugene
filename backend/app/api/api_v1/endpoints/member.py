from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, status
from app import crud, exceptions, schemas
from app.api import deps
from sqlalchemy.orm import Session
from app import models
router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.MemberOut)
def create_member(
    member_in: schemas.MemberCreate,
    workspace_in: models.Workspace = Depends(deps.get_current_workspace),
    db: Session = Depends(deps.get_db)
) -> models.Member:
    """Create member API

    Args:
        member_in (schemas.MemberCreate): Member data

    Returns:
        models.Member: returns member model
    """
    member = crud.member.create(db=db, obj_in=member_in)

    return member


@router.put("/{member_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.MemberOut)
def update_member(
    member_uuid: str,
    member_in: schemas.MemberUpdate,
    db: Session = Depends(deps.get_db)
) -> models.Member:
    member_obj = crud.member.get_by_uuid(db=db, uuid=member_uuid)
    member = crud.member.update(db=db, db_obj=member_obj, obj_in=member_in)

    return member
    
@router.get("/{member_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.MemberOut)
def update_member(
    member_uuid: str,
    db: Session = Depends(deps.get_db)
) -> models.Member:
    
    member = crud.member.get_by_uuid(db=db, uuid=member_uuid)
    return member


@router.delete("/{member_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.MemberOut)
def delete_member(
    member_uuid: str,
    db: Session = Depends(deps.get_db)
) -> models.Member:
    
    member = crud.member.delete_by_uuid(db=db, uuid=member_uuid)
    return member