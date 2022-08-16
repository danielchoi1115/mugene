
from fastapi import HTTPException, status


class BadRequestException(HTTPException):
    status_code = status.HTTP_400_BAD_REQUEST


class UserExistException(BadRequestException):
    def __init__(self) -> None:
        self.detail = "The user with this email already exists in the system"


class IncorrectLoginException(BadRequestException):
    def __init__(self) -> None:
        self.detail = "Incorrect username or password"
