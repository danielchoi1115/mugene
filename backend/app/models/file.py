from sqlalchemy import Column, Integer, BINARY, ForeignKey, VARCHAR, TIMESTAMP, CHAR, TEXT
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey
from sqlalchemy.orm import synonym

class File(Base):
    __tablename__ = "files"
    # Primary Keys
    file_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('file_id')
    
    # Unique Keys
    file_uuid = Column(BINARY(22), unique=True, nullable=False)
    uuid = synonym('file_uuid')
    
    # Foreign keys
    workspace_uuid = Column(BINARY(22), ForeignKey(pkey.workspaces_uuid), nullable=False)
    parent_file_uuid = Column(BINARY(22), ForeignKey(pkey.files_uuid), nullable=True)
    creator_uuid = Column(BINARY(22), ForeignKey(pkey.users_uuid), nullable=False)
    owner_uuid = Column(BINARY(22), ForeignKey(pkey.users_uuid), nullable=False)
    
    
    file_name = Column(VARCHAR(50), nullable=False)
    is_dir = Column(TINYINT(unsigned=True), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)
    file_type = Column(CHAR(50), nullable=True)
    file_url = Column(TEXT, nullable=True)
    size = Column(INTEGER(unsigned=True), nullable=True)
    