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
    is_folder: bool


class BlockCreate(BlockBase):
    block_name: str = Form()
    is_folder: bool = Form()
    parent_folder_id: int = Form(None)

class BlockUpdate(BlockBase):
    ...
    
class BlockInDB(BlockBase):
    block_id: Optional[int] = None
    creation_date: datetime
    created_by: Optional[int] = None
    file_type: Optional[str]
    file_url: Optional[str]
    size: Optional[int] = Field(default=None, gt=0, description="The file size must be greater than zero")
    parent_folder: Optional[int] = None

    class Config:
        orm_mode = True
        
class BlockOut(BlockInDB):
    ...
        
class Block(BlockInDB):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class BlockParent(BaseModel):
    parent_folder: PyObjectId = Field(default_factory=PyObjectId, alias="parent_folder.$id")
