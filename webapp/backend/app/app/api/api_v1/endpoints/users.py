from doctest import ELLIPSIS_MARKER
from typing import Any, List
import secrets
import logging
import os
import qrcode
import base64

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email

router = APIRouter()

qr_path = "/app/app/db/qr"
if not os.path.exists(qr_path):
    os.mkdir(qr_path)

logging.info(settings.SERVER_HOST)

# TODO add qr attribute to users database -> will make things simpler to code


def qr_exist(username: str) -> bool:
    qr = "{root}/{username}.png".format(root=qr_path, username=username)
    return os.path.isfile(qr)

def get_username(email)-> str:
    if isinstance(email, EmailStr):
        return str(email).split("'")[1].split("@")[0]
    return str(email).split("@")[0]

def encode_img(username) -> str:
    if qr_exist(username):
        return base64.b64encode(
        open("{root}/{username}.png".format(root=qr_path, username=username), "rb").read())
    else:
        return ''

def create_qr(user) -> None:
    route_login = "/account/login"
    username = get_username(user.email)
    link = "{host}{route_login}/{username}/{password}".format(
        host=settings.SERVER_HOST,
        route_login=route_login,
        username=user.email,
        password=user.password,
    )
    img = qrcode.make(link)
    path_img = qr_path + "/{id}.png".format(id=username)
    img.save(path_img) 

@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    if user_in.email == "generate@generated.com" and user_in.password == "generate":
        logging.info("Generating user...")
        username = secrets.token_urlsafe(10)
        user_in.email = username + "@generated.com"
        user_in.full_name = username
        user = crud.user.get_by_email(db, email=user_in.email)
        if user:
            logging.info("user already exist generated")
            raise HTTPException(
                status_code=400,
                detail="The user with this username already exists in the system.",
            )
        user_in.password = secrets.token_urlsafe(10)
        logging.info(user_in.email)
        logging.info(user_in.password)

        # save qr code
        create_qr(user_in)

        user = crud.user.create(db, obj_in=user_in)

        if not user_in.is_teacher and not user_in.is_superuser:
            std_in = schemas.StudentCreate(user_id=user.id)
            crud.student.create(db,obj_in=std_in)
        user.qr = encode_img(username)
        return user

    # create user using email
    user = crud.user.get_by_email(db, email=user_in.email)

    if user:
        logging.info("user already exist normal")
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )

    user = crud.user.create(db, obj_in=user_in)
    if user_in.is_teacher and not user_in.is_superuser:
        teacher_in = schemas.TeacherCreate(user_id=user.id)
        crud.teacher.create(db,obj_in=teacher_in)

    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )
    return user


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    else:
        user_in.password = None
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    username = get_username(current_user.email)
    current_user.qr = encode_img(username)
    return current_user


@router.post("/open", response_model=schemas.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(password=password, email=email, full_name=full_name)
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    # if user is student TODO give qr code
    user.qr = encode_img(get_username(user.email))
    return user


@router.get("/qr/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    username = get_username(user.email)
    user.qr = encode_img(username)
    return user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    # TODO update teacher/user updates delete also entries in database tables 
    logging.info(user_in)
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    if user_in.delete:
        logging.info("Deleting user " + str(user_id))
        # delete qr code if exist
        username = str(user.email).split("@")[0]
        qr_img = qr_path + "/{}.png".format(username)
        if os.path.exists(qr_img):
            os.remove(qr_img)

        if user.is_teacher:
            teacher = crud.teacher.get_by_user_id(db,user_id=user_id)
            teacher = crud.teacher.delete(db, id=teacher.id)
        elif not user.is_teacher:
            student = crud.student.get_by_user_id(db,user_id=user_id)
            student = crud.student.delete(db, id=student.id)

        user = crud.user.delete(db, id=user_id)

        return user
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    #TODO regenerate the qr code if password /username changes
    return user
