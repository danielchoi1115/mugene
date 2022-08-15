from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr, Field


class UserEmail(BaseModel):
    email: EmailStr


class UserBase(UserEmail):
    first_name: Optional[str]
    last_name: Optional[str]
    birthday: Optional[datetime]
    is_superuser: bool = False


class UserPost(UserBase):
    passwordHash: str


class UserResponseBase(BaseModel):
    result: bool


class UserResponse(UserResponseBase):
    user_id: str = Field(alias='_id')


class UserResponseError(UserResponseBase):
    result: bool = False
    exception: str
