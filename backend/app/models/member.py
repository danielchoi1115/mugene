from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class Member(Base):
    __tablename__ = "members"
    # Primary Keys
    member_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('member_id')
    
    # Foreign keys
    workspace_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.workspaces.id), nullable=False)
    user_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=False)
    
    member_level = Column(TINYINT(4), nullable=False, default=1)
    date_created = Column(TIMESTAMP, nullable=False)
    is_active = Column(TINYINT(4), nullable=False, default=1)