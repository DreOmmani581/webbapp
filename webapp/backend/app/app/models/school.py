from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
	from .user import User
	from .school import School
	from .viewer import Viewer


class School(Base):
	id = Column(Integer, primary_key=True, index=True)
	school_name = Column(String, index=True)
	project = relationship("Project", backref="school")
	viewer = relationship("Viewer", backref="school")