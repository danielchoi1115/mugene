from datetime import datetime
from fastapi import APIRouter, Depends, status
from app import crud, schemas
from app.schemas.dbref import RefWorkspace
from pymongo.client_session import ClientSession
from app.api import deps
from app.schemas.workspace import WorkspaceCreate, WorkspaceInDB
from app.crud.crud_workspace import CRUDWorkspace
router = APIRouter()

# 3


@router.get("/", status_code=200)
def get_work_space() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_work_space(
    workspace_in: WorkspaceCreate,
    session: ClientSession = Depends(deps.get_session)
) -> schemas.InsertResponse:
    """
    Root Get
    """
    # user.sampleId = RefUser(refid=user.sampleId.refid)
    # user.sma = [RefUser(refid=ref.refid) for ref in user.sma]

    # if not workspace_in.members:

    if workspace_in.created_by not in workspace_in.members:
        workspace_in.members.append(workspace_in.created_by)
    data = WorkspaceInDB(
        **workspace_in.dict(),
        creation_date=datetime.utcnow()
    )

    insertResert = crud.workspace.create(
        workspace_in_db=data,
        session=session
    )
    return insertResert
