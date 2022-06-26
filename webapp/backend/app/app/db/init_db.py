from sqlalchemy.orm import Session
import logging

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    # if you want to upgrade to new database of some other branch you first need to delete all tables 
    # and restart the backend. The alembic then will write new database scheme
    # https://stackoverflow.com/questions/30507853/how-to-clear-history-and-run-all-migrations-from-the-beginning

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        logging.info("import db user does not exist")
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            hash="",
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
