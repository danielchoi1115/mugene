from sqlalchemy import Column, BINARY, TEXT, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, FLOAT
from app.db.base_class import Base
from app.db.primary_keys import pkey

class Reportdata(Base):
    __tablename__ = "reportdata"
    # Primary Keys
    reportdata_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('reportdata_id')
    
    # Foreign keys
    sequence = Column(TEXT, nullable=True)
    sequence_file = Column(BINARY(22), nullable=True)