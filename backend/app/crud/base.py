from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """CRUD object with default methods to Create, Read, Update, Delete (CRUD).

    Args:
        `model`: A SQLAlchemy model class
        `schema`: A Pydantic model (schema) class
    """
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """ Base function for Read method

        Args:
            id (Any): primary key id

        Returns:
            Optional[ModelType]: returns sqlalchemy object
        """
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_by_uuid(self, db: Session, uuid: Any) -> Optional[ModelType]:
        """ Base function for Read method by uuid

        Args:
            uuid (Any): unique uuid

        Returns:
            Optional[ModelType]: returns sqlalchemy object
        """
        if type(uuid) == str:
            uuid = uuid.encode()
        return db.query(self.model).filter(self.model.uuid == uuid).first()
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """ Base function for Read multiple items

        Args:
            skip (int, optional): start position. Defaults to 0.
            limit (int, optional): number of records to read. Defaults to 100.

        Returns:
            List[ModelType]: returns list of sqlalchemy object
        """
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """ Base function for Create method

        Args:
            obj_in (CreateSchemaType): object model to be inserted

        Returns:
            ModelType: returns object model on success
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        """ Base function for Update method

        Args:
            obj_in (Union[UpdateSchemaType, Dict[str, Any]]): Object model to update

        Returns:
            ModelType: returns updated model
        """
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.merge(db_obj) 
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> ModelType:
        """ Base function for Delete method

        Args:
            uuid (Any): primary key id

        Returns:
            Optional[ModelType]: returns sqlalchemy object
        """
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
    
    def delete_by_uuid(self, db: Session, *, uuid: str) -> ModelType:
        """ Base function for Delete method by uuid

        Args:
            uuid (Any): unique uuid

        Returns:
            Optional[ModelType]: returns sqlalchemy object
        """
        obj = self.get_by_uuid(db=db, uuid=uuid)
        db.delete(obj)
        db.commit()
        return obj
    
    def check_if_null(self, value: Any) -> bool:
        if str(value) in ['none', 'null', '0']:
            return True
        return False