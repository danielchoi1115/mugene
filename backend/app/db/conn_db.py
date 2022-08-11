from app.db.init_client import client
from pymongo.database import Database
from pymongo.collection import Collection


class initDB:
    def __init__(self) -> None:
        self.client = client

    def getDB(self, dbName: str) -> Database | None:
        db_name_list = self.client.list_database_names()
        if dbName in db_name_list:
            return client[dbName]
        else:
            return None

    # def getCollection(self, collectionName: str) -> Collection | None:
    #     db_name_list = self.client.list_database_names()
    #     if dbName in db_name_list:
    #         return client[dbName]
    #     else:
    #         return None
