from fastapi import APIRouter

from app.api.api_v1.endpoints import file, user, workspace, auth, member, report

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(file.router, prefix="/file", tags=["file"])
api_router.include_router(workspace.router, prefix="/workspace", tags=["workspace"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(member.router, prefix="/member", tags=["member"])
api_router.include_router(report.router, prefix="/report", tags=["report"])
