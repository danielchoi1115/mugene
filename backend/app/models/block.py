from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP, CHAR, TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base

class Block(Base):
    __tablename__ = "blocks"
    block_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    block_name = Column(VARCHAR(50), unique=True, nullable=False)
    workspace_id = Column(INTEGER(unsigned=True), ForeignKey('workspaces.workspace_id'), nullable=False)
    is_folder = Column(TINYINT(unsigned=True), nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False)
    created_by = Column(INTEGER, ForeignKey('users.user_id'), nullable=False)
    file_type = Column(CHAR(50), nullable=True)
    file_url = Column(TEXT, nullable=True)
    size = Column(INTEGER(unsigned=True), nullable=True)
    parent_id = Column(INTEGER(unsigned=True), ForeignKey('blocks.block_id'), nullable=True)
    