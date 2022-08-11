
from pydantic import BaseModel
from app.schemas.dbref import RefUser
from app.schemas.permission import Permission


class Member(BaseModel):
    user: RefUser
    permission: Permission
