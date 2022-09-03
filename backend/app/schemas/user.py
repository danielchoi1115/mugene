from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, EmailStr, Field

AccountTypes = Literal["guest", "admin"]

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str]
    last_name: Optional[str]
    organization_code: str
    account_level: Literal[0,1,2,10]

class UserCreate(UserBase):
    email: EmailStr
    password: str
    
class UserUpdate(UserBase):
    ...

class UserInDB(UserBase):
    user_uuid: bytes = None
    hashed_password: str = None
    
    class Config:
        orm_mode = True

    
class UserOut(BaseModel):
    user_uuid: Optional[bytes]
    email: Optional[EmailStr] = None
    first_name: Optional[str]
    last_name: Optional[str]
    account_level: Optional[Literal[0,1,2,10]]
    date_created: Optional[datetime]
    organization_code: Optional[str]
    class Config:
        orm_mode = True
    # class Config:
    #     fields = {
    #         'hashed_password': {
    #             'exclude': True
    #         }
    #     }
