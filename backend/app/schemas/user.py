from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    is_superuser: bool = False
    organization: str


class UserIn(UserBase):
    password: str


class UserInDB(UserBase):
    creation_date: datetime
    hashed_password: str


# Additional properties to return via API
class User(UserInDB):
    ...
