from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, FLOAT
from app.db.base_class import Base
from app.db.primary_keys import pkey

class Report(Base):
    __tablename__ = "reports"
    report_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    
    workspace_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.workspaces.id), nullable=False)
    requestor_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=False)
    
    report_name = Column(VARCHAR(50), unique=True, nullable=False)
    
    processing_time = Column(FLOAT(unsigned=True), unique=True, nullable=True)
    date_requested = Column(TIMESTAMP, nullable=False)
    date_completed = Column(TIMESTAMP, nullable=False)