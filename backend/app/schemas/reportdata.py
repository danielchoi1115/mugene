from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel


class ReportdataBase(BaseModel):
    ...
    
class ReportdataCreate(ReportdataBase):
    ...
    
class ReportdataOut(ReportdataBase):
    report_id: Optional[int] = None