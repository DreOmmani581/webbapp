# Import all the models, so that Base has them before being
# imported by Alembic
import imp
from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.school import School
from app.models.user import User  # noqa
from app.models.teacher import Teacher
from app.models.project import Project
from app.models.student import Student
from app.models.data import Data 
from app.models.viewer import Viewer