from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, conlist


class MemberBase(BaseModel):
    member_level: Optional[int]
    is_active: Optional[bool]
    
class MemberCreate(MemberBase):
    workspace_id: int
    user_id: int
    member_level: int
    is_active: bool
    
class MemberUpdate(MemberBase):
    ...
    
class MemberInDB(MemberCreate):
    member_id: Optional[int] = None
    class Config:
        orm_mode = True
        
class MemberOut(MemberInDB):
    ...