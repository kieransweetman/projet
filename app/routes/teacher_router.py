from typing import List
from fastapi import APIRouter, Depends, HTTPException, Body, status

from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.teacher_base import TeacherCreate, TeacherBase, TeacherUpdate
from controllers.teacher_collection import (
    get_all_teachers,
    by_id,
    create,
    delete_teacher as delete_by_id,
    update,
)

router = APIRouter(prefix="/teacher", tags=["teacher"])


@router.get(
    "/",
    # response_model=List[dict]
    response_description="Get all teacher",
)
def get_teachers():
    try:
        return get_all_teachers()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id}", response_model=TeacherBase)
def get_teacher(id: str):
    try:
        teacher = by_id(id)
        return teacher

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/",
    response_model=TeacherBase,
    response_description="Create a new teacher",
    status_code=status.HTTP_201_CREATED,
)
def create_teacher(teacher: TeacherBase = Body(...)):
    try:
        return create(teacher)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/{id}",
    response_description="Delete a teacher",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_teacher(id: str):
    try:
        delete_by_id(id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch(
    "/{id}",
    response_model=TeacherBase,
    response_description="Update a teacher",
    status_code=status.HTTP_200_OK,
)
def update_teacher(
    id: str,
    teacher: TeacherBase = Body(...),
):
    try:
        update(teacher, id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
