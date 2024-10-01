from typing import List
from fastapi import APIRouter, HTTPException, status, Body


from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.class_base import (
    ClassCollection,
    ClassBase,
    ClassCreate,
    ClassUpdate,
    EmbeddedStudent,
)

from controllers.class_controller import get_all, new, add_student, get_students


router = APIRouter(prefix="/class", tags=["class"])


@router.get(
    "/",
    response_model=ClassCollection,
    response_description="Get all classs",
    response_model_by_alias=True,
    status_code=status.HTTP_200_OK,
)
def get_classs():
    try:
        class_ = get_all()
        return class_

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/",
    response_model=ClassBase,
    response_description="Create a new class",
    response_model_by_alias=True,
    status_code=status.HTTP_201_CREATED,
)
def new_class(class_: ClassCreate = Body(...)):
    try:
        created_class = new(class_)
        return created_class

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch(
    "/{id}/add_students",
    response_model=ClassBase,
    response_description="add student to class",
    response_model_by_alias=True,
    status_code=status.HTTP_200_OK,
)
def append_student(id: str, students: List[EmbeddedStudent] = Body(...)):
    try:
        class_ = add_student(id, students)
        return class_

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{id}/students",
    # response_model=List[EmbeddedStudent],
    response_description="Get all students in a class",
    response_model_by_alias=True,
    status_code=status.HTTP_200_OK,
)
def students_in_class(id: str):
    try:
        students = get_students(id)
        return students

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
