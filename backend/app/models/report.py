from sqlalchemy import Column, Integer, BINARY, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, FLOAT
from app.db.base_class import Base
from app.db.primary_keys import pkey

class Report(Base):
    __tablename__ = "reports"
    # Primary Keys
    report_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('report_id')
    
    # Unique Keys
    report_uuid = Column(BINARY(22), unique=True, nullable=False)
    uuid = synonym('report_uuid')
    
    # Foreign keys
    workspace_uuid = Column(BINARY(22), ForeignKey(pkey.workspaces_uuid), nullable=False)
    requestor_uuid = Column(BINARY(22), ForeignKey(pkey.users_uuid), nullable=False)
    reportdata_uuid = Column(BINARY(22), ForeignKey(pkey.reportdata_uuid), nullable=False)
    
    report_name = Column(VARCHAR(50), nullable=False)
    
    processing_time = Column(FLOAT(unsigned=True), nullable=True)
    date_requested = Column(TIMESTAMP, nullable=False)
    
    report_status = Column(TINYINT, nullable=False, default=0)
    date_completed = Column(TIMESTAMP, nullable=True)