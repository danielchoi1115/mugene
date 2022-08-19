from typing import Literal
from pydantic import BaseModel


class Permission(BaseModel):
    type: Literal["full", "read", "modify", "read-write", "delete"]
