from typing import TYPE_CHECKING, Text

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import PickleType , ARRAY

from app.db.base_class import Base

if TYPE_CHECKING:
	from .school import School 
	from .data import Data
	from .student import Student
	from .teacher import Teacher

class Project(Base):
	id = Column(Integer, primary_key=True, index=True)
	teacher_id = Column(Integer, ForeignKey("teacher.id"))
	project_name = Column(String, index=True)
	group_name = Column(String, index=True)
	description = Column(String, index=True)
	links = Column(String, index=True)
	school_id = Column(Integer, ForeignKey("school.id"))
	owner_id = Column(Integer, ForeignKey("user.id"))
	vote_counter = Column(Integer,index=True)
	data = relationship("Data", backref="project")
	student = relationship("Student", backref="project")
