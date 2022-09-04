
from datetime import datetime
from typing import Any, Dict, Optional
from app.crud.base import CRUDBase
from app import models
from app.schemas.member import MemberCreate, MemberUpdate
from sqlalchemy.orm import Session
from app.utils import B64UUID

class CRUDMember(CRUDBase[models.Member, MemberCreate, MemberUpdate]):
    def get(self, db: Session, id: Any) -> Optional[models.Member]:
        return db.query(self.model).filter(self.model.member_id == id).first()
    
    def create(self, db: Session, *, 
               obj_in: MemberCreate, 
               workspace_in: models.Workspace) -> models.Member:
        if isinstance(obj_in, dict):
            create_data = obj_in
        else:
            create_data = obj_in.dict(exclude_unset=True)
        db_obj = models.Member(**create_data)
        db_obj.workspace_uuid = workspace_in.workspace_uuid
        db_obj.member_uuid = B64UUID().bytes
        db_obj.date_created = datetime.utcnow()
        db.add(db_obj)
        db.commit()
        return db_obj

    def update(
        self, db: Session, *, db_obj: models.Member, obj_in: MemberUpdate | Dict[str, Any]
    ) -> models.Member:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)    
member = CRUDMember(models.Member)