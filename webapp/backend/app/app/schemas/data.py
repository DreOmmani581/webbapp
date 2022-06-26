from typing import Optional

from pydantic import BaseModel


# Shared properties
class DataBase(BaseModel):
    # Basics infos of data
    file_name: Optional[str] = None


# Properties to receive on data creation
class DataCreate(DataBase):
    project_id: int = None


# Properties to receive on data update
class DataUpdate(DataBase):
    pass


# Properties shared by models stored in DB
class DataInDBBase(DataBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Data(DataInDBBase):
    pass


# Properties properties stored in DB
class DataInDB(DataInDBBase):
    pass
