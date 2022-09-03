from datetime import datetime
import os
from typing import List
from app import exceptions
from app.crud.base import CRUDBase
from app.db.init_client import client
from app.schemas.file import FileCreate, FileUpdate
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app import models
from app import schemas
from app.schemas.pyobjectid import PyObjectId
from app.utils import B64UUID

class CRUDFile(CRUDBase[models.File, FileCreate, FileUpdate]):
    async def create(
        self,
        db: Session,
        file_in: schemas.FileCreate,
        file: UploadFile,
        user_in: models.User,
        workspace_in: models.Workspace,
    ) -> models.File:
        
        file_type = None
        file_url = None
        size = None

        if file:
            content = await file.read()
            size = len(content)
            filename, file_type = os.path.splitext(file.filename)
            file_url = filename
        
        if type(file_in.parent_file_uuid) == str:
            file_in.parent_file_uuid = file_in.parent_file_uuid.encode()
        
        db_obj = models.File(
            file_uuid=B64UUID().bytes,
            workspace_uuid=workspace_in.workspace_uuid,
            creator_uuid=user_in.user_uuid,
            owner_uuid=user_in.user_uuid,
            file_name=file_in.file_name,
            is_dir=file_in.is_dir,
            parent_file_uuid=file_in.parent_file_uuid,
            date_created=datetime.utcnow(),
            file_type=file_type,
            file_url=file_url,
            size=size,
        )
        
        db.add(db_obj)
        db.commit()

        return db_obj
    
    def get_multi(
        self, 
        db: Session, 
        workspace_id: int,
        *,  
        parent_file_id: int|str = None,
        skip: int = 0, 
        limit: int = 100
    ) -> List[models.File]:
        if parent_file_id:
            if self.check_if_null(parent_file_id):
                parent_file_id = None
            return db.query(self.model).filter(
                    self.model.parent_file_id == parent_file_id,
                    self.model.workspace_id == workspace_id
                ).offset(skip).limit(limit).all()
        
        return db.query(self.model).filter(
                self.model.workspace_id == workspace_id
            ).offset(skip).limit(limit).all()


file = CRUDFile(models.File)
