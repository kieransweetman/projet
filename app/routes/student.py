from typing import List
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.student_base import StudentBase, StudentCollection
from fastapi import APIRouter, HTTPException, status, Body

from schemas.student_base import (
    StudentCollection,
    StudentBase,
    StudentCreate,
    EmbeddedGrade,
    StudentUpdate,
)

from controllers.student_controller import (
    get_all,
    new,
    get_one,
    get_grades,
    delete,
    update,
)


router = APIRouter(prefix="/students", tags=["students"])


@router.get(
    "/",
    response_model=StudentCollection,
    response_description="Get all students",
    response_model_by_alias=True,
    status_code=status.HTTP_200_OK,
)
def get_students():
    try:

        students = get_all()
        return students

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{id}",
    response_model=StudentBase,
    response_description="Get One Student",
    status_code=status.HTTP_200_OK,
)
def get_one_student(id: str):
    try:
        student = get_one(id)
        return student

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{id}/grades",
    response_model=List[EmbeddedGrade],
    response_description="Get One Student Grades",
)
def get_student_grades(id: str):
    try:
        grades = get_grades(id)
        return grades

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="Delete One Student",
)
def delete_student(id: str):
    try:
        delete(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch(
    "/{id}",
    response_model=StudentBase,
    status_code=status.HTTP_200_OK,
    response_description="Update One Student",
)
def update_student(id: str, update_data: StudentUpdate = Body(...)):
    try:
        update(id, update_data)

        student = get_one(id)

        return student

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/",
    response_model=StudentBase,
    response_description="Create a new student",
    # response_model_by_alias=True,
    status_code=status.HTTP_201_CREATED,
)
def new_student(student: StudentCreate = Body(...)):
    try:
        created_student = new(student)
        return created_student

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
