from app.crud.projections.user import UserAuthProjection, UserProjection
from app.db.init_client import client
from app.schemas.user import User, UserCreate, UserInDB
from app import schemas
from app.core.security import get_password_hash
import json
from bson import json_util
from pydantic import EmailStr
from pymongo.client_session import ClientSession


def parse_json(data):
    return json.loads(json_util.dumps(data))


class CRUDUser():
    def create(self, user_in: UserCreate) -> schemas.InsertResponse | schemas.InsertResponseError:
        insert_result = False
        try:
            # data = jsonable_encoder(user)
            # data = {
            #     'name': "haha",
            #     'ref': [DBRef('user', id=PyObjectId("62f5224267a50432a59508f9"))]
            # }
            create_data = user_in.dict(by_alias=True)
            password = create_data.pop("password")
            user_in_db = UserInDB(**create_data,
                                  hashed_password=get_password_hash(password)
                                  )

            res = client['user_db']['users'].insert_one(
                user_in_db.dict(by_alias=True)
            )
            insert_result = res.acknowledged

            return schemas.InsertResponse(
                result=insert_result,
                _id=str(res.inserted_id)
            )
        except Exception as ex:
            return schemas.InsertResponseError(
                result=insert_result,
                exception=str(ex)
            )

    def get_by_email(self, email: EmailStr) -> User:
        # if projection is None:
        #     projection = UserProjection()
        try:
            res = client['user_db']['users'].find_one(
                filter={"email": email},
                # projection=projection.dict()
            )
            return User(**res)
        except Exception as e:
            raise

    def get_hashed_password(self, email: EmailStr) -> UserInDB:
        # if projection is None:
        #     projection = UserProjection()
        try:
            res = client['user_db']['users'].find_one(
                filter={"email": email}
            )
            return UserInDB(**res)
        except Exception as e:
            raise

    def login_user():
        pass


user = CRUDUser()
