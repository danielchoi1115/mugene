from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP, CHAR, TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base

class Workspace(Base):
    __tablename__ = "workspaces"
    workspace_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    workspace_name = Column(VARCHAR(50), unique=True, nullable=False)
    created_by = Column(INTEGER(unsigned=True), ForeignKey('users.user_id'), nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False)