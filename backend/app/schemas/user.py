from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, EmailStr, Field

AccountTypes = Literal["guest", "admin"]

class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    account_level: Literal[0,1,2,10]
    organization_code: str

class UserIn(UserBase):
    password: str


class UserInDB(UserBase):
    creation_date: datetime
    hashed_password: str

class User(UserInDB):
    ...
    
class UserOut(UserInDB):
    class Config:
        fields = {
            'hashed_password': {
                'exclude': True
            }
        }
