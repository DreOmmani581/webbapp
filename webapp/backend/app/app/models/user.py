from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401
    from .school import School
    from .teacher import Teacher
    from .student import Student
    from .user import User
    


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")

    is_teacher = Column(Boolean(), default=False)
    has_voted = Column(Boolean(), default=False)
    #student = relationship("Student", back_populates="user")
    #teacher = relationship("Teacher",back_populates="user")