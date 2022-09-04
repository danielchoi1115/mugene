from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import Form


class FileBase(BaseModel):
    file_name: Optional[str]
    parent_file_uuid: Optional[bytes] = None

class FileCreate(FileBase):
    file_name: str = Form(None)
    is_dir: bool = Form()
    parent_file_uuid: str = Form(None)

class FileUpdate(FileBase):
    ...
    
class FileOut(FileBase):
    file_id: Optional[int] = None
    workspace_uuid: Optional[bytes] = None
    creator_uuid: Optional[bytes] = None
    owner_uuid: Optional[bytes] = None
    file_name: str
    is_dir: bool
    parent_file_uuid: Optional[bytes] = None
    date_created: datetime
    file_type: Optional[str]
    file_url: Optional[str]
    size: Optional[int]
    
    class Config:
        orm_mode = True