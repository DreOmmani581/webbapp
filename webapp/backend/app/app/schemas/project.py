from typing import Optional

from pydantic import BaseModel


# Shared properties
class ProjectBase(BaseModel):
    # Basics infos of project
    project_name: Optional[str] = None
    group_name: Optional[str] = None
    description: Optional[str] = None
    links: Optional[str] = None
    vote_counter: Optional[int] = None
    #data = relationship("Data", backref="project")
    #student = relationship("Student", backref="project")


# Properties to receive on project creation
class ProjectCreate(ProjectBase):
    teacher_id: int = None
    school_id: int = None


# Properties to receive on project update
class ProjectUpdate(ProjectBase):
    pass


# Properties shared by models stored in DB
class ProjectInDBBase(ProjectBase):
    id: int
    owner_id: int
    school_id: int
    teacher_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Project(ProjectInDBBase):
    pass


# Properties properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass
