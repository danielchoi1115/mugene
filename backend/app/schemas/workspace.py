from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, conlist
from app.schemas.member import Member


class WorkspaceBase(BaseModel):
    workspace_name: str

class WorkspaceCreate(WorkspaceBase):
    ...
    
class WorkspaceUpdate(WorkspaceBase):
    ...

class WorkspaceInDB(WorkspaceBase):
    workspace_id: Optional[int] = None
    class Config:
        orm_mode = True
        
class WorkspaceOut(WorkspaceInDB):
    ...