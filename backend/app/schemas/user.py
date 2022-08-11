from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr, Field
from app.schemas.dbref import RefUser


class UserBase(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: Optional[str] = Field(alias='FN')
    last_name: Optional[str]
    birthday: Optional[datetime]
    is_superuser: bool = False
    sampleId: RefUser
    sma: List[RefUser]
    email: Optional[EmailStr] = None


class UserPost(UserBase):
    email: EmailStr
    passwordHash: str


# class UserCreate(UserBase):
#     sampleId: DBRef
#     sma: List[DBRef]
