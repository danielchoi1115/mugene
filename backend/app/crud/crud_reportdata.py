from datetime import datetime
from typing import Any, Dict, List, Optional
from app import schemas
from app.crud.base import CRUDBase
from app.db.init_client import client

from app import models
from sqlalchemy.orm import Session
from app.utils import B64UUID

class CRUDReportdata(CRUDBase[models.Reportdata, schemas.ReportdataCreate, schemas.ReportdataUpdate]):
    def create(
        self, 
        db: Session, 
        *, 
        obj_in: schemas.ReportCreate
    ) -> models.Reportdata:
        
        if isinstance(obj_in, dict):
            create_data = obj_in
        else:
            create_data = obj_in.dict(exclude_unset=True)
            
        db_obj = models.Reportdata(**create_data)
        db_obj.reportdata_uuid = B64UUID().bytes
        db.add(db_obj)
        db.commit()
        return db_obj 
    
reportdata = CRUDReportdata(models.Reportdata)
