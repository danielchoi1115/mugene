from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, conlist


class WorkspaceBase(BaseModel):
    workspace_name: str

class WorkspaceCreate(WorkspaceBase):
    ...
    
class WorkspaceUpdate(WorkspaceBase):
    owner_uuid: Optional[bytes] = None

class WorkspaceInDB(WorkspaceBase):
    workspace_uuid: Optional[bytes] = None
    class Config:
        orm_mode = True
        
class WorkspaceOut(BaseModel):
    workspace_uuid: Optional[bytes]
    creator_uuid: Optional[bytes] = None
    owner_uuid: Optional[bytes] = None
    workspace_name: str
    date_created: datetime
    class Config:
        orm_mode = True