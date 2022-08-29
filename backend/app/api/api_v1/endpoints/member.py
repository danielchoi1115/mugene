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
    db: Session = Depends(deps.get_db)
) -> models.Member:
    """
    Root Get
    """
    member = crud.member.create(db=db, obj_in=member_in)

    return member


@router.put("/{member_id}", status_code=status.HTTP_200_OK, response_model=schemas.MemberOut)
def update_member(
    member_id: int,
    member_in: schemas.MemberUpdate,
    db: Session = Depends(deps.get_db)
) -> models.Member:
    member_obj = crud.member.get(db=db, id=member_id)
    member = crud.member.update(db=db, db_obj=member_obj, obj_in=member_in)

    return member
    