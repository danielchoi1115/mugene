

from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app import models
from app.schemas.user import UserCreate, UserUpdate
from app.utils import B64UUID
from datetime import datetime
from app.core.security import get_password_hash

class CRUDUser(CRUDBase[models.User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[models.User]:
        return db.query(models.User).filter(models.User.email == email).first()
    
    def create(self, db: Session, *, obj_in: UserCreate) -> models.User:
        create_data = obj_in.dict()
        create_data.pop("password")
        db_obj = models.User(**create_data)
        db_obj.user_uuid = B64UUID().bytes
        db_obj.hashed_password = get_password_hash(obj_in.password)
        db_obj.date_created = datetime.utcnow()
        db.add(db_obj)
        db.commit()

        return db_obj
    
    def update(
        self, db: Session, *, db_obj: models.User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> models.User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def is_superuser(self, user: models.User) -> bool:
        return user.account_level == 10
    

user = CRUDUser(models.User)