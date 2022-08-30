from . import base

class NoWorkspaceException(base.UnauthorizedException):
    def __init__(self) -> None:
        self.detail = "Workspace not found"