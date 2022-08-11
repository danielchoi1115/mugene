from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.schemas.dbref import DBRefBase
# from bson import DBRef


class BlockBase(BaseModel):
    name: str
    size: int = Field(gt=0, description="The file size must be greater than zero")
    fileUrl: str

    class Config:
        arbitrary_types_allowed = True


class BlockCreate(BlockBase):
    name: str
    isFolder: bool
    creationDate: datetime
    fileType: str
    size: int = Field(gt=0, description="The file size must be greater than zero")
    fileUrl: str
    parentFolder: DBRefBase | None = None
    childFolders: List[DBRefBase] = []
    created_by: str

    class Config:
        arbitrary_types_allowed = True
