from typing import Optional

from pydantic import BaseModel


# Shared properties
class TeacherBase(BaseModel):
    pass


# Properties to receive on Teacher creation
class TeacherCreate(TeacherBase):
    user_id: int


# Properties to receive on Teacher update
class TeacherUpdate(TeacherBase):
    pass


# Properties shared by models stored in DB
class TeacherInDBBase(TeacherBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Teacher(TeacherInDBBase):
    pass


# Properties properties stored in DB
class TeacherInDB(TeacherInDBBase):
    pass
