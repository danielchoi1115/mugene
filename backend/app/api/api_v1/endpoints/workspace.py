from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, status
from app import crud, exceptions, schemas
from app.schemas.dbref import RefWorkspace
from pymongo.client_session import ClientSession
from app.api import deps
from app.schemas.member import Member
from app.schemas.pyobjectid import PyObjectId
from app.schemas.workspace import WorkspaceIn, WorkspaceInDB
from app.crud.crud_workspace import CRUDWorkspace
router = APIRouter()

# 3


@router.get("/", status_code=200)
def get_workspace() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_workspace(
    workspace_in: WorkspaceIn,
    session: ClientSession = Depends(deps.get_session)
) -> schemas.InsertResponse:
    """
    Root Get
    """
    # user.sampleId = RefUser(refid=user.sampleId.refid)
    # user.sma = [RefUser(refid=ref.refid) for ref in user.sma]

    # if not workspace_in.members:
    
    user = crud.user.get_by_id(workspace_in.created_by.user_ref.id)
    if not user:
        raise exceptions.NoUserFoundException
    
    if workspace_in.created_by not in workspace_in.members:
        workspace_in.members.append(workspace_in.created_by)
        
    data = WorkspaceInDB(
        **workspace_in.dict(by_alias=True),
        creation_date=datetime.utcnow()
    )

    insertResert = crud.workspace.create(
        workspace_in_db=data,
        session=session
    )
    return insertResert

@router.put("/members", status_code=status.HTTP_200_OK)
def update_members(
    workspace_id: PyObjectId,
    members: List[Member],
    session: ClientSession = Depends(deps.get_session)
) -> schemas.UpdateResponse:
    
    update_result = crud.workspace.add_members(
        workspace_id=workspace_id,
        members=members,
        session=session
    )
    return update_result
    
@router.put("/members/{memberId}", status_code=status.HTTP_201_CREATED)
def create_workspace(
    list: WorkspaceIn,
    session: ClientSession = Depends(deps.get_session)
) -> schemas.UpdateResponse:
    ... 