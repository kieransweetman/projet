from typing import List
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.student_base import StudentBase, StudentCollection


router = APIRouter(prefix="/students", tags=["students"])


@router.get(
    "/", response_model=StudentCollection, response_description="Get all students"
)
def get_students(db: PyMongoDatabase = Depends(Database.get_db)):
    try:
        students = StudentCollection(students=db["student"].find().to_list())
        return students

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}",response_model=StudentBase, response_description="Get One Student")
def get_one_student(id:str, db: PyMongoDatabase = Depends(Database.get_db)):
    try:
        # students = db.query(StudentBase).filter(StudentBase.id == codecli).first()
        student = db["student"].find_one({"_id":ObjectId(id)})
        return student

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,response_description="Delete One Student")
def delete_student(id:str, db: PyMongoDatabase = Depends(Database.get_db)):
    try:
        db["student"].delete_one({"_id":ObjectId(id)})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.patch("{id}",status_code=status.HTTP_200_OK,response_description="Update One Student")
# def update_student(id: str, db: PyMongoDatabase = Depends(Database.get_db)):
#     try:
#         db["student"].find_one_and_update("_id" == id)
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))