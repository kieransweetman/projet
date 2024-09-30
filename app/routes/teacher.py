from typing import List
from fastapi import APIRouter, HTTPException, status


from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.teacher_base import (
    TeacherCollection,
    TeacherBase,
    TeacherCreate,
    TeacherUpdate,
)

from controllers.teacher_controller import get_all, new


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
