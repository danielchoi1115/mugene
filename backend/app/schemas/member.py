
from typing import Literal
from pydantic import BaseModel
from app.schemas.dbref import DBRefBase, RefUser

from bson.dbref import DBRef


class Member(BaseModel):
    user_ref: RefUser
    permission: Literal["full", "read", "modify", "read-write", "delete"]

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if type(v) == dict:
            v = Member(**v)
        return v

    # @classmethod
    # def __modify_schema__(cls, field_schema):
    #     field_schema.update(type="string")
