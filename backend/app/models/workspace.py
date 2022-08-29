from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP, CHAR, TEXT
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class Workspace(Base):
    __tablename__ = "workspaces"
    # Primary Keys
    workspace_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('workspace_id')
    
    # Foreign keys
    creator_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=False)
    owner_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=False)
    
    workspace_name = Column(VARCHAR(50), unique=True, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)