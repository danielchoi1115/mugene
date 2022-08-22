from typing import List
from app import exceptions
from app.db.init_client import client
from app.schemas.block import Block, BlockInDB, BlockParent
from bson import json_util
import json
# from bson.dbref import DBRef
from bson.objectid import ObjectId
from pymongo.client_session import ClientSession
import json
from bson import ObjectId

from app import schemas
from app.schemas.pyobjectid import PyObjectId


class CRUDBlock():
    async def create(
        self,
        storage_id: str,
        block_in_db: BlockInDB,
        session: ClientSession
    ) -> schemas.InsertResponse:
        insert_result = False
        collection = client['storage_db'][storage_id]
        if block_in_db.parent_folder is not None:
            res = collection.find_one(block_in_db.parent_folder.refid)
            if not res:
                raise exceptions.NoParentFolderException

        try:
            session.start_transaction()
            res = collection.insert_one(
                block_in_db.dict(by_alias=True)
            )
            session.commit_transaction()
            insert_result = res.acknowledged

            return schemas.InsertResponse(
                result=insert_result,
                _id=str(res.inserted_id)
            )
        except Exception as ex:
            session.abort_transaction()
            raise schemas.InsertResponseError(
                result=insert_result,
                exception=str(ex)
            )

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
