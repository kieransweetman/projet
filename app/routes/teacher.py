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

from controllers.teacher_controller import get_all, get_one, new


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
def delete_teacher(id: str, db: PyMongoDatabase = Depends(Database.get_db)):
    try:
        db["teacher"].delete_one({"_id": ObjectId(id)})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch(
    "/{id}",
    response_model=TeacherBase,
    status_code=status.HTTP_200_OK,
    response_description="Update One Teacher",
)
def update_teacher(
    id: str, update_data: TeacherBase, db: PyMongoDatabase = Depends(Database.get_db)
):
    try:
        update_dict = update_data.model_dump(exclude_unset=True)
        updated = db["teacher"].update_one({"_id": ObjectId(id)}, {"$set": update_dict})

        teacher = get_one(id)

        return teacher

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))