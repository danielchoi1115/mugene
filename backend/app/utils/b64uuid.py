from base64 import urlsafe_b64encode #urlsafe_b64decode
import uuid
from uuid import UUID

# uuid that is base64 encoded
class B64UUID():
    """Instances of the UUID class with urlsafe base 64 encoded"""
    def __init__(self, uuid_: bytes | UUID = None) -> None:
        if type(uuid_) == bytes:
            self.uuid = UUID(bytes=uuid_)
        elif type(uuid_) == UUID:
            self.uuid = uuid_
        else:
            self.uuid = uuid.uuid4()

    @property
    def bytes(self):
        return urlsafe_b64encode(self.uuid.bytes).rstrip(b'=')
    # def slug2uuid(slug):
    #     if type(slug) == bytes:
    #         slug = slug.decode('ascii')
    #     return str(UUID(bytes=urlsafe_b64decode(slug + '==')))