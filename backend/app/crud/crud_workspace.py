
from datetime import datetime
from typing import List
from app import schemas
from app.db.init_client import client
from pymongo.client_session import ClientSession
from app import models
from sqlalchemy.orm import Session

class CRUDWorkspace():
    def create(self, db: Session, *, user_in: models.User, obj_in: schemas.WorkspaceCreate) -> models.User:
        create_data = obj_in.dict()
        db_obj = models.Workspace(**create_data)
        db_obj.created_by = user_in.user_id
        db_obj.creation_date = datetime.now()
        db.add(db_obj)
        db.commit()
        return db_obj 
  
    def update(self, filter, update, session: ClientSession, upsert=True) -> schemas.UpdateResponse:
        try:
            session.start_transaction()
            res = client['workspace_db']['workspaces'].update_many(
                filter,
                update,
                upsert=False
            )

            session.commit_transaction()
            insert_result = res
            return None
        except Exception as ex:
            session.abort_transaction()
            raise
workspace = CRUDWorkspace()
