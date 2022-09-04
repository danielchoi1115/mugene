from . import base


class UploadException(base.BadRequestException):
    def __init__(self) -> None:
        self.detail = "A directory cannot have file data. To upload a file, please set is_dir false"


class NullFileException(base.BadRequestException):
    """A file cannot be empty when 'is_dir' is false. Please upload a file or set 'is_dir' true"""
    def __init__(self) -> None:
        self.detail = "A file cannot be empty when 'is_dir' is false. Please upload a file or set 'is_dir' true"


class NoParentFolderException(base.AcceptedException):
    def __init__(self) -> None:
        self.detail = "Request was successful. But failed to proceed since parent folder is not found."

class NullDirectoryName(base.AcceptedException):
    def __init__(self) -> None:
        self.detail = "Directory name cannot be null."

class DuplicatedName(base.AcceptedException):
    def __init__(self) -> None:
        self.detail = "File name already exists."