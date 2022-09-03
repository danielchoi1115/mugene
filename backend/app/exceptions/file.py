from . import base


class UploadException(base.BadRequestException):
    def __init__(self) -> None:
        self.detail = "A directory cannot have file data. To upload a file, please set is_dir false"


class NullFileException(base.BadRequestException):
    def __init__(self) -> None:
        self.detail = "A file cannot be empty when 'is_dir' is false. Please upload a file or set 'is_dir' true"


class NoParentFolderException(base.AcceptedException):
    def __init__(self) -> None:
        self.detail = "Request was successful. But failed to proceed since parent folder is not found."
