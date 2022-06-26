from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.data import Data
from app.schemas.data import DataCreate, DataUpdate

import logging


class CRUDData(CRUDBase[Data, DataCreate, DataUpdate]):
    def create(
        self,
        db: Session,
        *,
        obj_in: DataCreate,
    ) -> Data:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_project(
        self, db: Session, *, project_id: int, skip: int = 0, limit: int = 100
    ) -> List[Data]:
        return (
            db.query(self.model)
            .filter(Data.project_id == project_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

data = CRUDData(Data)
