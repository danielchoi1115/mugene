from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from app.db.base_class import Base
from app.db.primary_keys import pkey

class PaidTarget(Base):
    __tablename__ = "paid_targets"
    # Primary Keys
    paid_target_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)  # 2
    id = synonym('paid_target_id')
    
    # Foreign keys
    workspace_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.workspaces_id), nullable=False)
    target_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.targets_id), nullable=False)
    payer_id = Column(INTEGER(unsigned=True), ForeignKey(pkey.users_id), nullable=False)
    
    date_paid = Column(TIMESTAMP, nullable=False)
    