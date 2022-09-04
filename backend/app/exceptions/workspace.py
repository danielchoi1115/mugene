from . import base

class MissingWorkspaceHeaderException(base.UnauthorizedException):
    def __init__(self) -> None:
        self.detail = "Workspace header is missing"

class WorkspaceNotFoundException(base.UnauthorizedException):
    def __init__(self) -> None:
        self.detail = "Workspace not found"

class InactiveWorkspace(base.AcceptedException):
    """Inactive Workspace"""
    def __init__(self) -> None:
        self.detail = "Inactive Workspace"
