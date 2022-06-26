from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

import os, logging

router = APIRouter()

qr_path = "/app/app/db/projects"
if not os.path.exists(qr_path):
    os.mkdir(qr_path)


@router.get("/", response_model=List[schemas.Project])
def read_projects(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve project.
    """
    if crud.user.is_superuser(current_user):
        projects = crud.project.get_multi(db, skip=skip, limit=limit)
    else:
        projects = crud.project.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return projects


@router.post("/", response_model=schemas.Project)
def create_project(
    *,
    db: Session = Depends(deps.get_db),
    project_in: schemas.ProjectCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new project.
    """
    # test with example users
    # project_in.teacher_id = 2
    # project_in.school_id = 1
    project = crud.project.create(db=db, obj_in=project_in, owner_id=current_user.id)
    project_upload_path = "/app/app/db/projects/{id}".format(id=project.id)
    if not os.path.exists(project_upload_path):
        os.mkdir(project_upload_path)
    return project


@router.get("/", response_model=List[schemas.Project])
def read_projects(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve project.
    """
    if crud.user.is_superuser(current_user):
        projects = crud.project.get_multi(db, skip=skip, limit=limit)
    else:
        projects = crud.project.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return projects


@router.get("/upload/{id}/{filename}")
async def read_file_by_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    filename: str,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    datas = crud.data.get_multi_by_project(db=db, project_id=id, skip=skip, limit=limit)
    file_path = ""
    for i in datas:
        if filename == os.path.basename(i.file_name):
            file_path = i.file_name
            break
    if file_path == "":
        raise HTTPException(status_code=404, detail="File not found")
    response = FileResponse(path=file_path, filename=os.path.basename(file_path))
    def iterfile():  
        with open(file_path, mode="rb") as file_like:  
            yield from file_like
    return StreamingResponse(iterfile(), media_type=response.media_type)

@router.get("/upload/{id}")
async def read_files_by_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    datas = crud.data.get_multi_by_project(db=db, project_id=id, skip=skip, limit=limit)
    l: List[FileResponse] = []
    datas = crud.data.get_multi_by_project(db=db, project_id=id, skip=skip, limit=limit)
    for i in datas:
         l.append(FileResponse(path=i.file_name, filename=os.path.basename(i.file_name)))
    return l

@router.post("/upload/{id}")
async def upload_file(
    *, db: Session = Depends(deps.get_db), id: int, files: List[UploadFile] = File(...)
):
    # TODO add premissions
    project_path = "/app/app/db/projects/{id}".format(id=id)
    if not os.path.exists(project_path):
        return {"info": "project does not exist ! create project first"}
    file_loc = project_path + f"/{files[0].filename}"
    with open(file_loc, "wb+") as file_object:
        file_object.write(files[0].file.read())

    # write file path to db
    exist = False
    datas = crud.data.get_multi_by_project(db=db, project_id=id)
    for i in datas:
        if i.file_name == file_loc:
            exist = True
            break
    
    if not exist:
        data_in = schemas.DataCreate(project_id=id, file_name=file_loc)
        crud.data.create(db=db, obj_in=data_in)

    return {"info": f"file '{files[0].filename}' saved at '{file_loc}'"}


@router.put("/{id}", response_model=schemas.Project)
def update_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    project_in: schemas.ProjectUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an project.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not crud.user.is_superuser(current_user) and (
        project.owner_id != current_user.id
    ):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    project = crud.project.update(db=db, db_obj=project, obj_in=project_in)
    return project


# THIS SHOULD BE TEMPORARY WORKAROUND FOR VIEWS VOTING
# PRETTY SURE IT IS VERY BAD TO ALLOW UPDATES WITHOUT ANY SORT OF LOGIN
@router.put("/vote/{id}", response_model=schemas.Project)
def vote(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    # project_in: schemas.ProjectUpdate,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an project.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    # if not crud.user.is_superuser(current_user) and (project.owner_id != current_user.id):
    #    raise HTTPException(status_code=400, detail="Not enough permissions")
    project_in = schemas.ProjectUpdate(vote_counter=project.vote_counter + 1)
    project = crud.project.update(db=db, db_obj=project, obj_in=project_in)
    return project


@router.get("/{id}", response_model=schemas.Project)
def read_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get project by ID.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not crud.user.is_superuser(current_user) and (
        project.owner_id != current_user.id
    ):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return project


@router.get("/school/{id}", response_model=List[schemas.Project])
def read_projects_by_school(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve project by school id.
    """
    projects = crud.project.get_multi_by_school(
        db=db, school_id=id, skip=skip, limit=limit
    )
    return projects


@router.delete("/{id}", response_model=schemas.Project)
def delete_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an project.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="project not found")
    if not crud.user.is_superuser(current_user) and (
        project.owner_id != current_user.id
    ):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    # remove project files when deleting the project
    files = crud.data.get_multi_by_project(db=db, project_id=id)
    logging.info(files)
    project_path = "/app/app/db/projects/{id}".format(id=id)
    for i in files:
        logging.info(i.file_name)
        os.remove(i.file_name)
        logging.info(i.id)
        crud.data.remove(db=db, id=i.id)
    os.rmdir(project_path)

    project = crud.project.remove(db=db, id=id)

    return project
