from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.schemas.dbref import DBRefBase, RefBlock
from .pyobjectid import PyObjectId
from fastapi import Form
from bson.objectid import ObjectId
# from bson import DBRef


class BlockBase(BaseModel):
    block_name: str
    parent_block_id: Optional[int] = None

class BlockCreate(BlockBase):
    block_name: str = Form()
    is_folder: bool = Form()
    parent_block_id: int = Form(None)

class BlockUpdate(BlockBase):
    ...
    
class BlockOut(BlockBase):
    block_id: Optional[int] = None
    workspace_id: Optional[int] = None
    parent_block_id: Optional[int] = None
    creator_id: Optional[int] = None
    owner_id: Optional[int] = None
    block_name: str
    is_folder: bool
    date_created: datetime
    file_type: Optional[str]
    file_url: Optional[str]
    size: Optional[int]
    
    class Config:
        orm_mode = True