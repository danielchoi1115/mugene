
from fastapi import HTTPException, status


class UnauthorizedException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED


class AcceptedException(HTTPException):
    status_code = status.HTTP_202_ACCEPTED


class BadRequestException(HTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
