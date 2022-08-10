from fastapi import APIRouter
from schemas.block import Block
from crud.crud_block import *
router = APIRouter()

# 3
@router.post("/", status_code=202)
def createBlock(block: Block) -> dict:
    """
    Post Block
    """
    
    return insertBlock(block)