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

from utils.common import COLLECTION


router = APIRouter(prefix="/teachers", tags=["teachers"])
collection = Database().get_db().get_collection(COLLECTION.STUDENT.value)


@router.get(
    "/",
    response_model=TeacherCollection,
    response_description="Get all teachers",
    response_model_by_alias=True,
    status_code=status.HTTP_200_OK,
)
def get_teachers():
    try:
        teachers = TeacherCollection(teachers=collection.find().to_list())
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
        model = teacher.model_dump(by_alias=True, exclude=["id"])

        new_id = collection.insert_one(model).inserted_id
        created_teacher = collection.find_one({"_id": new_id})

        print(created_teacher)
        return created_teacher

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
