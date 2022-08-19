from datetime import datetime
from fastapi import APIRouter, Depends, status
from app import schemas
from app.schemas.block import BlockCreate, BlockInDB
from app import crud
from app.api import deps
from pymongo.client_session import ClientSession

router = APIRouter()


@router.get("/{blockId}", status_code=status.HTTP_201_CREATED)
def getBlock(blockId: str, start: int = 0, end: int = 0) -> dict:
    # validateStorage()
    # validateBlock()
    return crud.block.read_many(blockId, start, end)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_block(
    storage_id: str,
    block_in: BlockCreate,
    session: ClientSession = Depends(deps.get_session)
) -> schemas.InsertResponse:
    """
    Post Block
    """
    # validateStorage()
    # validateBlock()

    # fileType: str
    # fileUrl: str
    # size
    data = BlockInDB(
        **block_in.dict(),
        creation_date=datetime.utcnow(),
        file_type='ss',
        file_url="ss",
        size=5
    )
    insertResult = crud.block.create(storage_id, data, session)
    return insertResult
