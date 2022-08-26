from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base

class Member(Base):
    __tablename__ = "members"
    member_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    workspace_id = Column(INTEGER(unsigned=True), ForeignKey('workspaces.workspace_id'), nullable=False)
    user_id = Column(INTEGER(unsigned=True), ForeignKey('users.user_id'), nullable=False)
    member_level = Column(TINYINT(4), nullable=False, default=1)
    join_date = Column(TIMESTAMP, nullable=False)
    is_active = Column(TINYINT(4), nullable=False, default=1)