from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

import os, logging

router = APIRouter()

# logging.info(get_file_path("123","123.txt"))

@router.get("/", response_model=List[schemas.School])
def read_schools(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve school.
    """
    if crud.user.is_superuser(current_user):
        schools = crud.school.get_multi(db, skip=skip, limit=limit)
    else:
        schools = []
    return schools


@router.post("/", response_model=schemas.School)
def create_school(
    *,
    db: Session = Depends(deps.get_db),
    school_in: schemas.SchoolCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new school.
    """
    school = crud.school.create(db=db, obj_in=school_in)
    return school


@router.put("/{id}", response_model=schemas.School)
def update_school(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    school_in: schemas.SchoolUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an school.
    """
    school = crud.school.get(db=db, id=id)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    # if not crud.user.is_superuser(current_user) and (school.owner_id != current_user.id):
    #    raise HTTPException(status_code=400, detail="Not enough permissions")
    school = crud.school.update(db=db, db_obj=school, obj_in=school_in)
    return school

@router.get("/{id}", response_model=schemas.School)
def read_school(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get school by ID.
    """
    school = crud.school.get(db=db, id=id)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    # if not crud.user.is_superuser(current_user) and (school.owner_id != current_user.id):
    #    raise HTTPException(status_code=400, detail="Not enough permissions")
    return school


@router.delete("/{id}", response_model=schemas.School)
def delete_school(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an school.
    """
    school = crud.school.get(db=db, id=id)
    if not school:
        raise HTTPException(status_code=404, detail="school not found")
    # if not crud.user.is_superuser(current_user) and (school.owner_id != current_user.id):
    #    raise HTTPException(status_code=400, detail="Not enough permissions")
    school = crud.school.remove(db=db, id=id)
    return school
