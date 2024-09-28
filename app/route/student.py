from typing import List
from fastapi import APIRouter, Depends, HTTPException


from config.database import Database
from pymongo.database import Database as PyMongoDatabase


router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=List[dict], response_description="Get all students")
def get_students(db: PyMongoDatabase = Depends(Database.get_db)):
    try:
        students = db["eleve"].find().to_list()
        return students

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
