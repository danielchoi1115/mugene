from fastapi import APIRouter

router = APIRouter()

# 3
@router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}