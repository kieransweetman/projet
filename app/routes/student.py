from typing import List
from fastapi import APIRouter, Depends, HTTPException, Body, status

from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.student_base import StudentCreate, StudentBase


router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=List[dict], response_description="Get all students")
def get_students(db: PyMongoDatabase = Depends(Database.get_db)):
    try:
        students = db["eleve"].find().to_list()
        return students

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/",
    response_model=StudentBase,
    response_description="Create a new student",
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student: StudentBase = Body(...), db: PyMongoDatabase = Depends(Database.get_db)
):
    try:
        new_student = db["student"].insert_one(
            student.model_dump(by_alias=True, exclude=["id"])
        )

        created = db["student"].find_one({"_id": new_student.inserted_id})
        return created

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
