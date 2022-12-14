from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class Target(Base):
    __tablename__ = "targets"
    # Primary Keys
    target_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('target_id')
    
    target_name = Column(String(256), nullable=True)
    access_level = Column(TINYINT(4), nullable=False, default=1)
    date_uploaded = Column(TIMESTAMP, nullable=False)