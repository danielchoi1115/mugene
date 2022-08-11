from fastapi import APIRouter
from app.schemas.block import BlockCreate
from app.crud.crud_block import CRUDBlock
router = APIRouter()


@router.get("/{blockId}", status_code=202)
def getBlock(blockId: str, start: int = 0, end: int = 0) -> dict:
    # validateStorage()
    # validateBlock()
    return CRUDBlock.read_many(blockId, start, end)


@router.post("/", status_code=202)
def makeBlock(block: BlockCreate) -> dict:
    """
    Post Block
    """
    # validateStorage()
    # validateBlock()
    return CRUDBlock.create(block)
