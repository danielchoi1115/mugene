from datetime import datetime
import os
from typing import List
from app import exceptions
from app.db.init_client import client
from app.schemas.block import Block
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app import models
from app import schemas
from app.schemas.pyobjectid import PyObjectId


class CRUDBlock():
    async def create(
        self,
        workspace_id: int,
        block_in: schemas.BlockCreate,
        file: UploadFile,
        db: Session,
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
            block_name=block_in.block_name,
            workspace_id=workspace_id,
            is_folder=block_in.is_folder,
            creation_date=datetime.utcnow(),
            created_by=user_in.user_id,
            file_type=file_type,
            file_url=file_url,
            size=size,
            parent_folder=block_in.parent_folder_id,
        )
        
        db.add(db_obj)
        db.commit()

        return db_obj

    def read_many(
        self,
        workspace_id: str,
        parent_id: PyObjectId = None,
        find_by_parents: bool = True,
        start: int = 0,
        end: int = 0
    ) -> List[Block]:
        filter_ = {}
        if find_by_parents:
            filter_ = {"parent_folder.$id": parent_id}
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


block = CRUDBlock()
