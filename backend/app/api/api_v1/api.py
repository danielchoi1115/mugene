from fastapi import APIRouter

from app.api.api_v1.endpoints import user, block, workspace

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(block.router, prefix="/block", tags=["block"])
api_router.include_router(workspace.router, prefix="/work", tags=["work"])
