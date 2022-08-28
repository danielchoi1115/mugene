from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP, CHAR, TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey
from sqlalchemy.orm import synonym

class Block(Base):
    __tablename__ = "blocks"
    block_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('block_id')
    workspace_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.workspaces.id), nullable=False)
    parent_block_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=True)
    creator_id = Column(INTEGER, ForeignKey(pkey.users.id), nullable=False)
    
    block_name = Column(VARCHAR(50), unique=True, nullable=False)
    is_folder = Column(TINYINT(unsigned=True), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)
    file_type = Column(CHAR(50), nullable=True)
    file_url = Column(TEXT, nullable=True)
    size = Column(INTEGER(unsigned=True), nullable=True)
    