from typing import Literal
from pydantic import BaseModel


class Permission(BaseModel):
    type: Literal["full", "read", "modify", "read-write", "delete"]

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if type(v) == dict:
            v = Permission(**v)
        return v

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
