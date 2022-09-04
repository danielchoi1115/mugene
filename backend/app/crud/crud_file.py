from datetime import datetime
import os
from typing import List, Optional
from app import exceptions
from app.crud.base import CRUDBase
from app.schemas.file import FileCreate, FileUpdate
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app import models
from app import schemas
from app.utils import B64UUID

class CRUDFile(CRUDBase[models.File, FileCreate, FileUpdate]):
    def get_by_filename(
            self, 
            db: Session, 
            workspace_in: models.Workspace,
            parent_file_uuid: str | bytes | None,
            file_name: str
        ) -> Optional[models.File]:
        if type(parent_file_uuid) == str:
            parent_file_uuid = parent_file_uuid.encode()
            
        return db.query(self.model).filter(
            self.model.file_name == file_name,
            self.model.workspace_uuid == workspace_in.workspace_uuid,
            self.model.parent_file_uuid == parent_file_uuid
        ).first()
    
    async def create(
        self,
        db: Session,
        file_in: schemas.FileCreate,
        filedata: UploadFile,
        user_in: models.User,
        workspace_in: models.Workspace,
    ) -> models.File:
        
        file_type = None
        file_url = None
        size = None
        if filedata:
            content = await filedata.read()
            size = len(content)
            filename, file_type = os.path.splitext(filedata.filename)
            file_url = filename
        
        if type(file_in.parent_file_uuid) == str:
            file_in.parent_file_uuid = file_in.parent_file_uuid.encode()
        
        if not file_in.file_name:
            if file_in.is_dir:
                raise exceptions.NullDirectoryName
            else:
                file_in.file_name = filedata.filename
        
        file = self.get_by_filename(
            db=db,
            workspace_in=workspace_in,
            parent_file_uuid=file_in.parent_file_uuid,
            file_name = file_in.file_name
        )
        if file:
            raise exceptions.DuplicatedName
        
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
        workspace_uuid: int,
        *,  
        parent_file_uuid: int|str = None,
        skip: int = 0, 
        limit: int = 100
    ) -> List[models.File]:
        if parent_file_uuid:
            if self.check_if_null(parent_file_uuid):
                parent_file_uuid = None
            return db.query(self.model).filter(
                    self.model.parent_file_uuid == parent_file_uuid,
                    self.model.workspace_uuid == workspace_uuid
                ).offset(skip).limit(limit).all()
        
        return db.query(self.model).filter(
                self.model.workspace_uuid == workspace_uuid
            ).offset(skip).limit(limit).all()


file = CRUDFile(models.File)
