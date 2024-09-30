from typing import List
from fastapi import APIRouter, HTTPException, status, Body

from schemas.student_base import (
    StudentCollection,
    StudentBase,
    StudentCreate,
)

from controllers.student_controller import get_all, new


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
