from app.db.init_client import client
from app.schemas.user import UserPost
from fastapi.encoders import jsonable_encoder
import json
from bson import json_util


def parse_json(data):
    return json.loads(json_util.dumps(data))


class CRUDUser():
    def create(user: UserPost) -> dict:
        try:
            # data = jsonable_encoder(user)
            # data = {
            #     'name': "haha",
            #     'ref': [DBRef('user', id=PyObjectId("62f5224267a50432a59508f9"))]
            # }
            res = client['user_db']['users'].insert_one(
                user.dict(by_alias=True)
            )
            return {
                "insertResult": res.acknowledged,
                "_id": str(res.inserted_id)
            }
        except Exception as ex:
            print(ex)


user = CRUDUser()
