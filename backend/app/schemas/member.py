from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, conlist


class MemberBase(BaseModel):
    member_level: Optional[int]
    is_active: Optional[bool]
    
class MemberCreate(MemberBase):
    user_uuid: bytes
    member_level: int
    is_active: bool = True
    
class MemberUpdate(MemberBase):
    ...
        
class MemberOut(BaseModel):
    member_uuid: Optional[bytes] = None
    workspace_uuid: bytes
    user_uuid: bytes
    member_level: int
    is_active: bool
    class Config:
        orm_mode = True