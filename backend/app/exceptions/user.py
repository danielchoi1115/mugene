from . import base

class NoUserFoundException(base.AcceptedException):
    def __init__(self) -> None:
        self.detail = "Request was successful, but failed to preceed since no user was found. Please check the user ID"

class UserExistException(base.BadRequestException):
    def __init__(self) -> None:
        self.detail = "The user with this email already exists in the system"


class IncorrectLoginException(base.BadRequestException):
    def __init__(self) -> None:
        self.detail = "Incorrect username or password"
