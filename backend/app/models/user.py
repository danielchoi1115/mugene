from sqlalchemy import Column, BINARY, String, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class User(Base):
    __tablename__ = "users"
    # Primary Keys
    user_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('user_id')
    
    # Unique Keys
    user_uuid = Column(BINARY(22), unique=True, nullable=False)
    uuid = synonym('user_uuid')
    
    # Foreign keys
    approver_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users_id), nullable=False)
    
    email = Column(VARCHAR(256), unique=True, nullable=False)
    hashed_password = Column(VARCHAR(256), nullable=False)
    first_name = Column(String(256), nullable=True)
    last_name = Column(String(256), nullable=True)
    account_level = Column(TINYINT(4), nullable=False, default=0)
    date_created = Column(TIMESTAMP, nullable=False)
    organization_code = Column(VARCHAR(50), nullable=False)
    