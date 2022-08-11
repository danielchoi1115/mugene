from fastapi import APIRouter
from app.schemas.dbref import RefWorkSpace
from app.schemas.workspace import WorkSpaceCreate, WorkSpacePost
from app.crud.crud_work import CRUDWork
router = APIRouter()

# 3


@router.get("/", status_code=200)
def getWorkSpace() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@router.post("/", status_code=202)
def createWorkSpace(work: WorkSpacePost) -> dict:
    """
    Root Get
    """
    # user.sampleId = RefUser(refid=user.sampleId.refid)
    # user.sma = [RefUser(refid=ref.refid) for ref in user.sma]
    _work = WorkSpaceCreate(**work.dict())
    _work.owner = _work.createdBy
    insertResert = CRUDWork.create(_work)

    return insertResert
