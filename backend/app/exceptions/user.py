
from fastapi import HTTPException

UserExistException = HTTPException(  # 5
    status_code=400,
    detail="The user with this email already exists in the system",
)
