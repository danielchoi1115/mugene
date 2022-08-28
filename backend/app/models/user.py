from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class User(Base):
    __tablename__ = "users"
    user_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    
    approver_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=False)
    
    email = Column(VARCHAR(256), unique=True, nullable=False)
    hashed_password = Column(VARCHAR(256), nullable=False)
    first_name = Column(String(256), nullable=True)
    last_name = Column(String(256), nullable=True)
    account_level = Column(TINYINT(4), nullable=False, default=0)
    date_created = Column(TIMESTAMP, nullable=False)
    organization_code = Column(VARCHAR(50), nullable=False)
    