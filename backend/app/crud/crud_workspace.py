
from app import schemas
from app.db.init_client import client
from app.schemas.workspace import WorkspaceInDB
from pymongo.client_session import ClientSession


class CRUDWorkspace():
    def create(self, workspace_in_db: WorkspaceInDB, session: ClientSession) -> schemas.InsertResponse:
        insert_result = False
        try:
            session.start_transaction()
            res = client['workspace_db']['workspaces'].insert_one(
                workspace_in_db.dict(by_alias=True)
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


workspace = CRUDWorkspace()
