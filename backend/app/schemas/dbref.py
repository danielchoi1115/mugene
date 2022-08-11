from typing import Any
from pydantic import BaseModel, Field
from app.schemas.pyobjectid import PyObjectId
from app.db.db_config import (userdb_config, blockdb_config, workdb_config)
from bson.son import SON
from bson.dbref import DBRef as bsonDBRef


class DBRefBase(BaseModel):
    refid: PyObjectId = Field(default_factory=PyObjectId, alias="$id")

    class Config:
        allow_population_by_field_name = True


class RefUser(DBRefBase):
    ref: str = Field(userdb_config.COLLECTION, alias="$ref")
    db: str = Field(userdb_config.DB, alias="$db")


class RefBlock(DBRefBase):
    ref: str = Field(blockdb_config.COLLECTION, alias="$ref")
    db: str = Field(blockdb_config.DB, alias="$db")


class RefWorkSpace(DBRefBase):
    ref: str = Field(workdb_config.COLLECTION, alias="$ref")
    db: str = Field(workdb_config.DB, alias="$db")
# class DBRef(bsonDBRef):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         pass

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type="string")


# def RefUser(refid: PyObjectId):
#     return DBRef(
#         collection=userdb_config.COLLECTION,
#         database=userdb_config.DB,
#         id=refid
#     )


# def RefBlock(refid: PyObjectId):
#     return DBRef(
#         collection=blockdb_config.COLLECTION,
#         database=blockdb_config.DB,
#         id=refid
#     )
