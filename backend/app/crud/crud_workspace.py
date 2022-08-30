
from datetime import datetime
from typing import Any, Dict, List, Optional
from app import schemas
from app.crud.base import CRUDBase
from app.db.init_client import client
from pymongo.client_session import ClientSession
from app import models
from sqlalchemy.orm import Session
import uuid
class CRUDWorkspace(CRUDBase[models.Workspace, schemas.WorkspaceCreate, schemas.WorkspaceUpdate]):
    def get_by_uuid(self, db: Session, uuid: str) -> Optional[models.Workspace]:
        return db.query(self.model).filter(self.model.workspace_uuid == uuid).first()

    def create(self, db: Session, *, user_in: models.User, obj_in: schemas.WorkspaceCreate) -> models.Workspace:
        create_data = obj_in.dict()
        db_obj = models.Workspace(**create_data)
        db_obj.creator_id = user_in.user_id
        db_obj.owner_id = user_in.user_id
        db_obj.workspace_uuid = uuid.uuid4().hex
        db_obj.date_created = datetime.utcnow()
        db.add(db_obj)
        db.commit()
        return db_obj 
  
    def update(
        self, db: Session, *, db_obj: models.Workspace, obj_in: schemas.WorkspaceUpdate| Dict[str, Any]
    ) -> models.Workspace:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
workspace = CRUDWorkspace(models.Workspace)
