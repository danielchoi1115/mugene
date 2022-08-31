from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP
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
    user_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)