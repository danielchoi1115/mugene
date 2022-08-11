from app.db.init_client import client
from app.schemas.block import BlockCreate
from bson import json_util
import json
# from bson.dbref import DBRef
from bson.objectid import ObjectId

import json
from bson import ObjectId


class CRUDBlock():
    def create(block: BlockCreate):
        try:
            if block.parentFolder is not None:
                block.parentFolder = block.parentFolder.as_doc()
            res = client['storage_db']['62f3d5e306d48ff2df0dc4fa'].insert_one(
                block.dict()
            )
        except Exception as ex:
            print(ex)
            print(block)
        return {"insertResult": res.acknowledged}

    def read_many(blockId: str, start: int = 0, end: int = 0, projection: dict = None):
        res = client['storage_db']['62f3d5e306d48ff2df0dc4fa'].find_one(
            {'_id': ObjectId(blockId)}
        )
        if end - start > 10:
            end = start + 9
        if end < start:
            start = end
        res2 = client['storage_db']['62f3d5e306d48ff2df0dc4fa'].find(
            {}, limit=end-start+1, skip=start, projection={"_id": 1, "name": 1}
        )
        return parse_json(res2)


def parse_json(data):
    return json.loads(json_util.dumps(data))


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


block = CRUDBlock()
