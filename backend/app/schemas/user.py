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
    user_id: Optional[int] = None
    hashed_password: str = None
    
    class Config:
        orm_mode = True

    
class UserOut(UserInDB):
    class Config:
        fields = {
            'hashed_password': {
                'exclude': True
            }
        }
