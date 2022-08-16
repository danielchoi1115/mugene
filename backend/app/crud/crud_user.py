from app.crud.projections.user import UserProjection
from app.db.init_client import client
from app.schemas.user import User, UserCreate, UserInDB, UserResponse, UserResponseError
from app.core.security import get_password_hash
import json
from bson import json_util
from pydantic import EmailStr


def parse_json(data):
    return json.loads(json_util.dumps(data))


class CRUDUser():
    def create(self, user_in: UserCreate) -> UserResponse | UserResponseError:
        insert_result = False
        try:
            # data = jsonable_encoder(user)
            # data = {
            #     'name': "haha",
            #     'ref': [DBRef('user', id=PyObjectId("62f5224267a50432a59508f9"))]
            # }
            create_data = user_in.dict()
            password = create_data.pop("password")
            user_in_db = UserInDB(**create_data,
                                  hashed_password=get_password_hash(password)
                                  )

            res = client['user_db']['users'].insert_one(
                user_in_db.dict()
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

    def get_by_email(self, email: EmailStr, projection: UserProjection = None) -> UserInDB:
        # if projection is None:
        #     projection = UserProjection()
        res = client['user_db']['users'].find_one(
            filter={"email": email},
            # projection=projection.dict()
        )
        return UserInDB(**res)

    def login_user():
        pass


user = CRUDUser()
