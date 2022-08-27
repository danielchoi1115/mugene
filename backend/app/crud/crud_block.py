from datetime import datetime
import os
from typing import List
from app import exceptions
from app.crud.base import CRUDBase
from app.db.init_client import client
from app.schemas.block import Block, BlockCreate, BlockUpdate
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
            block_name=block_in.block_name,
            is_folder=block_in.is_folder,
            creation_date=datetime.utcnow(),
            created_by=user_in.user_id,
            file_type=file_type,
            file_url=file_url,
            size=size,
            parent_id=block_in.parent_id,
        )
        
        db.add(db_obj)
        db.commit()

        return db_obj
    
    def get_multi(
        self, 
        db: Session, 
        workspace_id: int,
        *, 
        find_by_parent: bool = True, 
        parent_id: int = None,
        skip: int = 0, 
        limit: int = 100
    ) -> List[models.Block]:
        if find_by_parent:
            return db.query(self.model).filter(
                    self.model.parent_id == parent_id,
                    self.model.workspace_id == workspace_id
                ).offset(skip).limit(limit).all()
        
        return db.query(self.model).filter(
                self.model.workspace_id == workspace_id
            ).offset(skip).limit(limit).all()
    
    def read_many(
        self,
        workspace_id: str,
        parent_id: int = None,
        find_by_parents: bool = True,
        start: int = 0,
        end: int = 0
    ) -> List[Block]:
        
        filter_ = {}
        if find_by_parents:
            filter_ = {"parent_id.$id": parent_id}
        res = client['storage_db'][workspace_id].find(
            filter=filter_
        )
        if end - start > 10:
            end = start + 9
        if end < start:
            start = end
        # res2 = client['storage_db']['62f3d5e306d48ff2df0dc4fa'].find(
        #     {}, limit=end-start+1, skip=start, projection={"_id": 1, "name": 1}
        # )
        read_result: List[Block] = [
            Block(**i) for i in res
        ]
        # return [block.dict() for block in read_result]
        return read_result


block = CRUDBlock(models.Block)
