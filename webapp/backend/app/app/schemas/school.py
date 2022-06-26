from typing import Optional

from pydantic import BaseModel


# Shared properties
class SchoolBase(BaseModel):
    # Basics infos of school
    school_name: Optional[str] = None


# Properties to receive on school creation
class SchoolCreate(SchoolBase):
    pass

# Properties to receive on school update
class SchoolUpdate(SchoolBase):
    pass


# Properties shared by models stored in DB
class SchoolInDBBase(SchoolBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class School(SchoolInDBBase):
    pass


# Properties properties stored in DB
class SchoolInDB(SchoolInDBBase):
    pass
