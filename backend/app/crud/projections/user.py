from pydantic import BaseModel, Field


class UserProjection(BaseModel):
    id: int = Field(default=1, alias='_id')
    hashed_password: int = 0


class UserAuthProjection(UserProjection):
    hashed_password: int = 1


class UserFullProjection(UserProjection):
    first_name: int = 1
    last_name: int = 1
    birthday: int = 1
    is_superuser: int = 1
