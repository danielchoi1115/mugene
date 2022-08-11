from app.db.init_client import client
from app.schemas.workspace import WorkSpaceCreate


class CRUDWork():
    def create(work: WorkSpaceCreate) -> dict:
        try:
            res = client['workspace_db']['workspaces'].insert_one(
                work.dict(by_alias=True)
            )
            return {
                "insertResult": res.acknowledged,
                "_id": str(res.inserted_id)
            }
        except Exception as ex:
            print(ex)


user = CRUDWork()
