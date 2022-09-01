
from datetime import datetime
from typing import Any, Dict, List, Optional
from app import schemas
from app.crud.base import CRUDBase
from app.db.init_client import client

from app import models
from sqlalchemy.orm import Session
from app.utils import B64UUID

class CRUDReport(CRUDBase[models.Report, schemas.ReportCreate, schemas.ReportUpdate]):
    def create(
        self, 
        db: Session, 
        *, 
        workspace_in: models.Workspace, 
        user_in: models.User,
        reportdata_in: models.Reportdata,
        obj_in: schemas.ReportCreate
    ) -> models.Report:
        
        if isinstance(obj_in, dict):
            create_data = obj_in
        else:
            create_data = obj_in.dict(exclude_unset=True)
        
        db_obj = models.Report(**create_data)
        db_obj.workspace_id = workspace_in.workspace_id
        db_obj.reportdata_id = reportdata_in.reportdata_id
        db_obj.requestor_id = user_in.user_id
        db_obj.date_requested = datetime.utcnow()
        db.add(db_obj)
        db.commit()
        return db_obj 
  
    def update(
        self, 
        db: Session, 
        *, 
        db_obj: models.Report, 
        obj_in: schemas.ReportUpdate
    ) -> models.Report:
        
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
report = CRUDReport(models.Report)
