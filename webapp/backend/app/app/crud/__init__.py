from .crud_item import item
from .crud_user import user
from .crud_project import project
from .crud_student import student
from .crud_teacher import teacher
from .crud_school import school
from .crud_data import data


# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
