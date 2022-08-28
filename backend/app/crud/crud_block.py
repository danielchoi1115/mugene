from datetime import datetime
import os
from typing import List
from app import exceptions
from app.crud.base import CRUDBase
from app.db.init_client import client
from app.schemas.block import BlockCreate, BlockUpdate
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app import models
from app import schemas
from app.schemas.pyobjectid import PyObjectId


class CRUDBlock(CRUDBase[models.Block, BlockCreate, BlockUpdate]):
    async def create(
        self,
        db: Session,
        workspace_id: int,
        block_in: schemas.BlockCreate,
        file: UploadFile,
        user_in: models.User,
    ) -> models.Block:
        
        file_type = None
        file_url = None
        size = None

        if file:
            content = await file.read()
            size = len(content)
            filename, file_type = os.path.splitext(file.filename)
            file_url = filename

        db_obj = models.Block(
            workspace_id=workspace_id,
            parent_block_id=block_in.parent_block_id,
            creator_id=user_in.user_id,
            owner_id=user_in.user_id,
            block_name=block_in.block_name,
            is_folder=block_in.is_folder,
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
        parent_block_id: int|str = None,
        skip: int = 0, 
        limit: int = 100
    ) -> List[models.Block]:
        if parent_block_id:
            if self.check_if_null(parent_block_id):
                parent_block_id = None
            return db.query(self.model).filter(
                    self.model.parent_block_id == parent_block_id,
                    self.model.workspace_id == workspace_id
                ).offset(skip).limit(limit).all()
        
        return db.query(self.model).filter(
                self.model.workspace_id == workspace_id
            ).offset(skip).limit(limit).all()


block = CRUDBlock(models.Block)
