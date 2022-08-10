from app.db.init_db import client
from app.schemas.block import Block
# from bson.dbref import DBRef
from bson.objectid import ObjectId

def getBlock(blockId: str):
    print(blockId)

def insertBlock(block: Block):
    try:
        block.parentFolder = block.parentFolder.as_doc()
        res = client['mugene']['blocks'].insert_one(
            block.dict()
        )
        print(res.acknowledged)
    except Exception as ex:
        print (ex)
        print(block)
    return {"insertResult": res.acknowledged}

