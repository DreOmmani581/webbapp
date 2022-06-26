from typing import Optional

from pydantic import BaseModel


# Shared properties
class StudentBase(BaseModel):
    project_id: Optional[int]


# Properties to receive on Student creation
class StudentCreate(StudentBase):
    user_id: int


# Properties to receive on Student update
class StudentUpdate(StudentBase):
    pass


# Properties shared by models stored in DB
class StudentInDBBase(StudentBase):
    id: int
    user_id: int
    project_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Student(StudentInDBBase):
    pass


# Properties properties stored in DB
class StudentInDB(StudentInDBBase):
    pass
