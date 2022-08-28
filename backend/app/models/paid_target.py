from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class PaidTarget(Base):
    __tablename__ = "paid_targets"
    paid_target_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    
    workspace_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.workspaces.id), nullable=False)
    target_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.targets.id), nullable=False)
    payer_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users.id), nullable=False)
    
    organization_code = Column(VARCHAR(50), nullable=False)
    