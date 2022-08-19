from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, conlist
from app.schemas.member import Member


class WorkspaceBase(BaseModel):
    workspace_name: str


class WorkspaceCreate(WorkspaceBase):
    created_by: Member
    members: List[Member]


class WorkspaceInDB(WorkspaceCreate):
    creation_date: datetime


class Workspace(WorkspaceInDB):
    ...
