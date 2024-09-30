from typing import List
from fastapi import APIRouter, HTTPException, status


from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.student_base import (
    StudentCollection,
    StudentBase,
    StudentCreate,
    StudentUpdate,
)

from utils.common import COLLECTION


router = APIRouter(prefix="/students", tags=["students"])
collection = Database().get_db().get_collection(COLLECTION.STUDENT.value)


@router.get(
    "/",
    response_model=StudentCollection,
    response_description="Get all students",
    response_model_by_alias=True,
)
def get_students():
    try:
        students = StudentCollection(students=collection.find().to_list())
        return students

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/",
    response_model=StudentBase,
    response_description="Create a new student",
    response_model_by_alias=True,
    status_code=status.HTTP_201_CREATED,
)
def new_student(student: StudentCreate):
    try:
        print("router Student: ", student)
        model = student.model_dump(by_alias=True)
        print("router: ", model)
        new_id = collection.insert_one(model).inserted_id
        print(new_id)
        created_student = collection.find_one({"_id": new_id})

        return created_student

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
