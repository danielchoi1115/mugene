from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel
from app.schemas.reportdata import ReportdataCreate

class ReportBase(BaseModel):
    report_name: Optional[str] = None
    
class ReportCreate(ReportBase):
    ...
    
class ReportUpdate(ReportBase):
    report_status: Optional[int] = None
    processing_time: Optional[float] = None
    date_completed: Optional[datetime] = None
    
class ReportOut(ReportBase):
    report_id: Optional[int] = None
    report_name: str
    date_requested: datetime
    report_status: int
    
    class Config:
        orm_mode = True