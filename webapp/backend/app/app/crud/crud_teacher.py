from typing import List, Optional, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate


class CRUDTeacher(CRUDBase[Teacher, TeacherCreate, TeacherUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: TeacherCreate, owner_id: int
    ) -> Teacher:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user_id(self, db: Session, user_id: Any) -> Optional[Teacher]:
        return db.query(self.model).filter(self.model.user_id == user_id).first()

    def delete(self, db: Session, *, id: int) -> Teacher:
        return super().remove(db=db,id=id)

    #def get_multi_by_owner(
    #    self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    #) -> List[Teacher]:
    #    return (
    #        db.query(self.model)
    #        .filter(Teacher.owner_id == owner_id)
    #        .offset(skip)
    #        .limit(limit)
    #        .all()
    #    )


teacher = CRUDTeacher(Teacher)
