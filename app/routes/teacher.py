from typing import List
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status


from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.teacher_base import (
    TeacherCollection,
    TeacherBase,
    TeacherCreate,
    TeacherUpdate,
)

from schemas.class_base import EmbeddedStudent

from schemas.student_base import StudentBase

from controllers.teacher_controller import (
    get_all,
    get_one,
    new,
    teachers_students,
    delete,
    update,
)


router = APIRouter(prefix="/teachers", tags=["teachers"])


@router.get(
    "/",
    response_model=TeacherCollection,
    response_description="Get all teachers",
    response_model_by_alias=True,
    status_code=status.HTTP_200_OK,
)
def get_teachers():
    try:
        teachers = get_all()
        return teachers

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/",
    response_model=TeacherBase,
    response_description="Create a new teacher",
    response_model_by_alias=True,
    status_code=status.HTTP_201_CREATED,
)
def new_teacher(teacher: TeacherCreate):
    try:
        created_teacher = new(teacher)
        return created_teacher

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="Delete One Teacher",
)
def delete_teacher(id: str):
    try:
        delete(id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch(
    "/{id}",
    response_model=TeacherBase,
    status_code=status.HTTP_200_OK,
    response_description="Update One Teacher",
)
def update_teacher(id: str, update_data: TeacherUpdate):
    try:

        teacher = update(id, update_data)

        return teacher

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{id}/students",
    response_model=List[EmbeddedStudent],
    status_code=status.HTTP_200_OK,
    response_description="Get all students of a teacher with grades",
)
def get_students(id: str):
    try:
        students = teachers_students(id)

        return students

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
