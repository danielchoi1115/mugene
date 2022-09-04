from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, conlist


class WorkspaceBase(BaseModel):
    workspace_name: str

class WorkspaceCreate(WorkspaceBase):
    ...
    
class WorkspaceUpdate(WorkspaceBase):
    workspace_name: Optional[str]
    owner_uuid: Optional[bytes] = None
    is_active: Optional[bool]
        
class WorkspaceOut(BaseModel):
    workspace_uuid: Optional[bytes]
    creator_uuid: Optional[bytes] = None
    owner_uuid: Optional[bytes] = None
    workspace_name: str
    date_created: datetime
    is_active: bool
    class Config:
        orm_mode = True