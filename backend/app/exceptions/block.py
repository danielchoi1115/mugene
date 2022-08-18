from . import base


class NoParentFolderException(base.AcceptedException):
    def __init__(self) -> None:
        self.detail = "Request was successful. But failed to proceed since parent folder is not found."
