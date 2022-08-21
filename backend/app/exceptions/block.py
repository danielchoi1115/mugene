from . import base


class FileAsFolderException(base.BadRequestException):
    def __init__(self) -> None:
        self.detail = "A directory cannot have file data. To upload a file, please set is_folder false"


class FileIsNullException(base.BadRequestException):
    def __init__(self) -> None:
        self.detail = "A file cannot be empty. You must upload a file if is_folder is false"


class NoParentFolderException(base.AcceptedException):
    def __init__(self) -> None:
        self.detail = "Request was successful. But failed to proceed since parent folder is not found."
