from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .school import School  # noqa: F401


class Viewer(Base):
    id = Column(Integer, primary_key=True, index=True)
    is_Voter = Column(Boolean(), default=False)
    has_voted = Column(Boolean(), default=False)
    school_id = Column(Integer, ForeignKey("school.id"))
