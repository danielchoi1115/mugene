from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel
from app.schemas.reportdata import ReportdataCreate

class ReportBase(BaseModel):
    report_name: Optional[str] = None
    
class ReportCreate(ReportBase):
    reportdata: ReportdataCreate
class ReportUpdate(ReportBase):
    ...
    
class ReportOut(ReportBase):
    report_id: Optional[int] = None
    report_name: str
    reportdata: ReportdataCreate
    
    class Config:
        orm_mode = True