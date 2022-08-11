from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from app.schemas.member import Member


class WorkSpace(BaseModel):
    workspace_name: str


class WorkSpacePost(WorkSpace):
    members: Optional[List[Member]] = []
    creationDate: datetime
    createdBy: Member


class WorkSpaceCreate(WorkSpacePost):
    owner: Member = None

    