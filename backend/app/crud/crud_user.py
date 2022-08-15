from app.db.init_client import client
from app.schemas.user import UserPost, UserEmail, UserResponse, UserResponseError
from fastapi.encoders import jsonable_encoder
import json
from bson import json_util


def parse_json(data):
    return json.loads(json_util.dumps(data))


class CRUDUser():
    def create(self, user: UserPost) -> UserResponse | UserResponseError:
        insert_result = False
        try:
            # data = jsonable_encoder(user)
            # data = {
            #     'name': "haha",
            #     'ref': [DBRef('user', id=PyObjectId("62f5224267a50432a59508f9"))]
            # }
            res = client['user_db']['users'].insert_one(
                user.dict(by_alias=True)
            )
            insert_result = res.acknowledged

            return UserResponse(
                result=insert_result,
                _id=str(res.inserted_id)
            )
        except Exception as ex:
            return UserResponseError(
                result=insert_result,
                exception=str(ex)
            )

    def get_by_email(self, user: UserEmail) -> dict:
        return client['user_db']['users'].find_one(
            user.dict()
        )


user = CRUDUser()
