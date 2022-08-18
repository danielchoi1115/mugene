from . import base


class CredentialException(base.UnauthorizedException):
    def __init__(self) -> None:
        self.detail = "Could not validate credentials"
        self.headers = {"WWW-Authenticate": "Bearer"}
