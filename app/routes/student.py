from typing import List
from fastapi import APIRouter, Depends, HTTPException


from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.student_base import StudentCreate, Student


router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=List[dict], response_description="Get all students")
def get_students(db: PyMongoDatabase = Depends(Database.get_db)):
    try:
        students = db["eleve"].find().to_list()
        return students

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=Student, response_description="Create a new student")
def create_student(
    student: StudentCreate, db: PyMongoDatabase = Depends(Database.get_db)
):
    try:
        student = Student(db["student"].insert_one(student))
        return student

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
