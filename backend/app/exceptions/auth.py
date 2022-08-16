
from fastapi import HTTPException, status


class UnauthorizedException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED


class CredentialException(UnauthorizedException):
    def __init__(self) -> None:
        self.detail = "Could not validate credentials"
        self.headers = {"WWW-Authenticate": "Bearer"}
