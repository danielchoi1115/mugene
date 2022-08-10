from datetime import datetime
from typing import List
from pydantic import BaseModel
# from blockRef import BlockRef
from app.schemas.dbRef import DBRef
# from bson import DBRef
class Block(BaseModel):
    _id: str
    name: str
    isFolder: bool
    creationDate: datetime
    fileType: str
    size: int
    fileUrl: str
    parentFolder: DBRef | None = None
    childFolders: List[DBRef] = []
    
    class Config:
        arbitrary_types_allowed = True