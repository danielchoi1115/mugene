from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from app import schemas
from app.schemas.block import BlockOut
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


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[BlockOut])
def get_many_blocks(
    parent_block_id: int|str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    workspace: models.Workspace = Depends(deps.get_current_workspace)
) -> List[models.Block]:
    # validateStorage()
    # validateBlock()
    
    read_result = crud.block.get_multi(
        workspace_id=workspace.workspace_id,
        parent_block_id=parent_block_id,
        skip=skip,
        limit=limit,
        db=db
    )
    
    return read_result


@router.post("/", status_code=status.HTTP_200_OK, response_model=schemas.BlockOut)
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
