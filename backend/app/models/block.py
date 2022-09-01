from sqlalchemy import Column, Integer, BINARY, ForeignKey, VARCHAR, TIMESTAMP, CHAR, TEXT
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey
from sqlalchemy.orm import synonym

class Block(Base):
    __tablename__ = "blocks"
    # Primary Keys
    block_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('block_id')
    
    # Unique Keys
    block_uuid = Column(BINARY(22), unique=True, nullable=False)
    uuid = synonym('block_uuid')
    
    # Foreign keys
    workspace_uuid = Column(BINARY(22), ForeignKey(pkey.workspaces), nullable=False)
    parent_block_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.blocks), nullable=True)
    creator_id = Column(INTEGER, ForeignKey(pkey.users), nullable=False)
    
    block_name = Column(VARCHAR(50), nullable=False)
    is_folder = Column(TINYINT(unsigned=True), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)
    file_type = Column(CHAR(50), nullable=True)
    file_url = Column(TEXT, nullable=True)
    size = Column(INTEGER(unsigned=True), nullable=True)
    