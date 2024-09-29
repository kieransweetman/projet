from typing import List
from fastapi import APIRouter, Depends, HTTPException, Body, status

from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.student_base import StudentCreate, StudentBase, StudentUpdate
from controllers.student_collection import (
    get_all_students,
    by_id,
    create,
    delete_student as delete_by_id,
    update,
)


router = APIRouter(prefix="/students", tags=["students"])


@router.get(
    "/",
    # response_model=List[dict]
    response_description="Get all students",
)
def get_students():
    try:
        return get_all_students()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id}", response_model=StudentBase)
def get_student(id: str):
    try:
        student = by_id(id)
        return student

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/",
    response_model=StudentBase,
    response_description="Create a new student",
    status_code=status.HTTP_201_CREATED,
)
def create_student(student: StudentCreate = Body(...)):
    try:
        return create(student)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/{id}",
    response_description="Delete a student",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_student(id: str):
    try:
        delete_by_id(id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch(
    "/{id}",
    response_model=StudentBase,
    response_description="Update a student",
    status_code=status.HTTP_200_OK,
)
def update_student(
    id: str,
    student: StudentUpdate = Body(...),
):
    try:
        update(student, id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
