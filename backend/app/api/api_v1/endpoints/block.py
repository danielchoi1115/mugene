from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from app import schemas
from app.schemas.block import Block
from app import crud
from app.api import deps
from pymongo.client_session import ClientSession
import os
from app.schemas.dbref import RefBlock, RefUser
from app import exceptions
from app.schemas.pyobjectid import PyObjectId
from sqlalchemy.orm import Session
from app import models
router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Block])
def get_many_blocks(
    find_by_parent: bool = True,
    parent_id: int = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    workspace_id: str = Depends(deps.get_current_workspace)
) -> List[Block]:
    # validateStorage()
    # validateBlock()
    
    read_result = crud.block.get_multi(
        workspace_id=workspace_id,
        find_by_parent=find_by_parent,
        parent_id=parent_id,
        skip=skip,
        limit=limit,
        db=db
    )
    
    return read_result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.BlockOut)
async def create_block(
    workspace_id: int,
    block_in: schemas.BlockCreate = Depends(schemas.BlockCreate),
    file: UploadFile = File(None),
    db: Session = Depends(deps.get_db),
    user_in: models.User = Depends(deps.get_current_user)
) -> models.Block:
    """
    Post Block
    """
    if file and block_in.is_folder:
        raise exceptions.FileAsFolderException
    elif file is None and not block_in.is_folder:
        raise exceptions.FileIsNullException
        
    block = await crud.block.create(
        workspace_id=workspace_id,
        block_in=block_in, 
        file=file,
        db=db,
        user_in=user_in
    )
    return block
