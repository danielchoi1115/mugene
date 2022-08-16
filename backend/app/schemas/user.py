from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    birthday: Optional[datetime]
    is_superuser: bool = False


class UserCreate(UserBase):
    password: str


class UserInDBBase(UserBase):
    class Config:
        orm_mode = True


class UserReturn(UserBase):
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    birthday: Optional[datetime]
    is_superuser: bool = False

# Additional properties stored in DB but not returned by API


class UserInDB(UserInDBBase):
    hashed_password: str


# Additional properties to return via API
class User(UserInDBBase):
    ...


class UserResponseBase(BaseModel):
    result: bool


class UserResponse(UserResponseBase):
    user_id: str = Field(alias='_id')


class UserResponseError(UserResponseBase):
    result: bool = False
    exception: str
