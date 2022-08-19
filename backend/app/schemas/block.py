from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.schemas.dbref import DBRefBase, RefBlock
from .pyobjectid import PyObjectId
from .member import Member
# from bson import DBRef


class BlockBase(BaseModel):
    name: str
    is_folder: bool


class BlockCreate(BlockBase):
    created_by: Member
    parent_folder: RefBlock = None

    class Config:
        arbitrary_types_allowed = True


class BlockInDB(BlockCreate):
    creation_date: datetime
    file_type: str
    file_url: str
    size: int = Field(gt=0, description="The file size must be greater than zero")
    child_folders: List[RefBlock] = []


class BlockParent(BaseModel):
    parent_folder: PyObjectId = Field(default_factory=PyObjectId, alias="parent_folder.$id")

