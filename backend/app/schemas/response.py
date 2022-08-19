from pydantic import BaseModel, Field


class InsertResponseBase(BaseModel):
    result: bool


class InsertResponse(InsertResponseBase):
    user_id: str = Field(alias='_id')


class InsertResponseError(InsertResponseBase):
    result: bool = False
    exception: str
