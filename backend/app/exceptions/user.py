from . import base


class UserExistException(base.BadRequestException):
    def __init__(self) -> None:
        self.detail = "The user with this email already exists in the system"


class IncorrectLoginException(base.BadRequestException):
    def __init__(self) -> None:
        self.detail = "Incorrect username or password"
