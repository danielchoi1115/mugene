from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from app import schemas
from app.schemas.block import Block, BlockIn, BlockInDB
from app import crud
from app.api import deps
from pymongo.client_session import ClientSession
import os
from app.schemas.dbref import RefBlock, RefUser
from app import exceptions
from app.schemas.member import Member
from app.schemas.pyobjectid import PyObjectId
from app.schemas.workspace import Workspace
router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Block])
def get_block(
    find_by_parents: bool = True,
    parent_id: PyObjectId = None,
    start: int = 0,
    end: int = 10,
    workspace_id: str = Depends(deps.get_current_workspace)
) -> List[Block]:
    # validateStorage()
    # validateBlock()
    read_result = crud.block.read_many(
        workspace_id=workspace_id,
        find_by_parents=find_by_parents,
        parent_id=parent_id,
        start=start,
        end=end
    )
    return read_result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_block(
    storage_id: str,
    block_in: BlockIn = Depends(BlockIn),
    session: ClientSession = Depends(deps.get_session),
    file: UploadFile = File(None)
) -> schemas.InsertResponse:
    """
    Post Block
    """
    # validateStorage()
    # validateBlock()

    file_type = 'directory'
    file_url = None
    size = None

    user_ref = RefUser(refid=block_in.creator_id)
    created_by = Member(user_ref=user_ref)

    if file and block_in.is_folder:
        raise exceptions.FileAsFolderException
    elif file is None and not block_in.is_folder:
        raise exceptions.FileIsNullException

    if file:
        content = await file.read()
        size = len(content)
        filename, file_type = os.path.splitext(file.filename)
        file_url = filename

    parent_folder = None
    if block_in.parent_folder_id:
        parent_folder = RefBlock(refid=block_in.parent_folder_id)

    data = BlockInDB(
        name=block_in.name,
        is_folder=block_in.is_folder,
        created_by=created_by,
        parent_folder=parent_folder,
        creation_date=datetime.utcnow(),
        file_type=file_type,
        file_url=file_url,
        size=size
    )
    insertResult = await crud.block.create(storage_id, data, session)
    return insertResult
