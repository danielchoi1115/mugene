from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP, CHAR, TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class Workspace(Base):
    __tablename__ = "workspaces"
    workspace_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    
    creator_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=False)
    owner_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=False)
    
    workspace_name = Column(VARCHAR(50), unique=True, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)