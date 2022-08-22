from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.schemas.dbref import DBRefBase, RefBlock
from .pyobjectid import PyObjectId
from .member import Member
from fastapi import Form
from bson.objectid import ObjectId
# from bson import DBRef


class BlockBase(BaseModel):
    name: str
    is_folder: bool


class BlockIn(BlockBase):
    name: str = Form()
    is_folder: bool = Form()
    creator_id: PyObjectId = Form()
    parent_folder_id: PyObjectId = Form(None)

    # class Config:
    #     arbitrary_types_allowed = True
    # @classmethod
    # def as_form(
    #     cls,
    #     name: str = Form(),
    #     is_folder: bool = Form(),
    #     creator_id: PyObjectId = Form(),
    #     parent_folder_id: PyObjectId = Form(None),

    # ) -> BlockIn:
    #     return cls(
    #         name=name,
    #         is_folder=is_folder,
    #         creator_id=creator_id,
    #         parent_folder_id=parent_folder_id
    #     )


class BlockInDB(BlockBase):
    creation_date: datetime
    created_by: Member
    file_type: Optional[str]
    file_url: Optional[str]
    size: Optional[int] = Field(default=None, gt=0, description="The file size must be greater than zero")
    parent_folder: Optional[DBRefBase] = None
    child_folders: List[DBRefBase] = []


class Block(BlockInDB):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class BlockParent(BaseModel):
    parent_folder: PyObjectId = Field(default_factory=PyObjectId, alias="parent_folder.$id")
