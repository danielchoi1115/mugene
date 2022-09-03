from sqlalchemy import Column, BINARY, String, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class Member(Base):
    __tablename__ = "members"
    # Primary Keys
    member_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('member_id')
    
    # Unique Keys
    member_uuid = Column(BINARY(22), unique=True, nullable=False)
    uuid = synonym('member_uuid')
    
    # Foreign keys
    workspace_uuid = Column(BINARY(22), ForeignKey(pkey.workspaces_uuid), nullable=False)
    user_uuid = Column(BINARY(22), ForeignKey(pkey.users_uuid), nullable=False)
    
    member_level = Column(TINYINT(4), nullable=False, default=1)
    date_created = Column(TIMESTAMP, nullable=False)
    is_active = Column(TINYINT(4), nullable=False, default=1)