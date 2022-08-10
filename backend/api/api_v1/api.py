from fastapi import APIRouter

from api_v1.endpoints import user, block

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(block.router, prefix="/block", tags=["block"])