from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .data import Data  # noqa: F401


class Data(Base):
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)
    project_id = Column(Integer, ForeignKey("project.id"))
