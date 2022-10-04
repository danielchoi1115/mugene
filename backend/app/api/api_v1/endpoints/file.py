from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from app import schemas
from app.schemas.file import FileOut
from app import crud
from app.api import deps
from pymongo.client_session import ClientSession
import os
from app import exceptions
from app.schemas.pyobjectid import PyObjectId
from sqlalchemy.orm import Session
from app import models
router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[FileOut])
def get_many_files(
    parent_file_id: int|str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    workspace: models.Workspace = Depends(deps.get_current_workspace)
) -> List[models.File]:
    """ get many files

    Args:
        parent_file_id (int | str, optional): parent file id. Defaults to None.
        skip (int, optional): start index. Defaults to 0.
        limit (int, optional): return limit. Defaults to 100.

    Returns:
        List[models.File]: List of file models
    """
    read_result = crud.file.get_multi(
        workspace_id=workspace.workspace_id,
        parent_file_id=parent_file_id,
        skip=skip,
        limit=limit,
        db=db
    )
    
    return read_result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.FileOut)
async def create_file(
    filedata: UploadFile = File(None),
    db: Session = Depends(deps.get_db),
    file_in: schemas.FileCreate = Depends(schemas.FileCreate),
    user_in: models.User = Depends(deps.get_current_user),
    workspace_in: models.Workspace = Depends(deps.get_current_workspace)
) -> models.File:
    """_summary_

    Args:
        filedata (UploadFile, optional): uploaded file. Defaults to File(None).

    Raises:
        exceptions.UploadException: If filedata exists
        exceptions.NullFileException: _description_

    Returns:
        models.File: _description_
    """
    if filedata and file_in.is_dir:
        raise exceptions.UploadException
    elif not filedata and file_in.is_dir == False:
        raise exceptions.NullFileException
    
    file = await crud.file.create(
        file_in=file_in, 
        filedata=filedata,
        db=db,
        user_in=user_in,
        workspace_in=workspace_in,
    )
    return file

@router.get("/{file_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.FileOut)
def get_file(
    file_uuid: str,
    db: Session = Depends(deps.get_db)
) -> models.File:
    
    file = crud.file.get_by_uuid(db=db, uuid=file_uuid)
    
    return file

@router.delete("/{file_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.FileOut)
def delete_file(
    file_uuid: str,
    db: Session = Depends(deps.get_db)
) -> models.File:
    
    read_result = crud.file.delete_by_uuid(db=db, uuid=file_uuid)
    
    return read_result