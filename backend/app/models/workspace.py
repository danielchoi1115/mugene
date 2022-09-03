from sqlalchemy import Column, Integer, BINARY, ForeignKey, VARCHAR, TIMESTAMP, CHAR, TEXT, BINARY
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class Workspace(Base):
    __tablename__ = "workspaces"
    # Primary Keys
    workspace_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('workspace_id')
    
    # Unique Keys
    workspace_uuid= Column(BINARY(22), unique=True, nullable=False)
    uuid = synonym('workspace_uuid')
    
    # Foreign keys
    creator_uuid = Column(BINARY(22), ForeignKey(pkey.users_uuid), nullable=False)
    owner_uuid = Column(BINARY(22), ForeignKey(pkey.users_uuid), nullable=False)
    
    workspace_name = Column(VARCHAR(50), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)