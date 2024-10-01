from typing import List
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status, Body


from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.class_base import (
    ClassCollection,
    ClassBase,
    ClassCreate,
    ClassUpdate,
    EmbeddedStudent,
)

from controllers.class_controller import get_all, get_one, new, add_student, get_students


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


@router.get("/{id}", response_model=ClassBase, response_description="Get One Class")
def get_one_class(id: str, db: PyMongoDatabase = Depends(Database.get_db)):
    try:
        class_ = db["class"].find_one({"_id": ObjectId(id)})
        return class_

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="Delete One Class",
)
def delete_class(id: str, db: PyMongoDatabase = Depends(Database.get_db)):
    try:
        db["class"].delete_one({"_id": ObjectId(id)})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch(
    "/{id}",
    response_model=ClassBase,
    status_code=status.HTTP_200_OK,
    response_description="Update One Class",
)
def update_class(
    id: str,
    update_data: ClassUpdate = Body(...),
    db: PyMongoDatabase = Depends(Database.get_db),
):
    try:
        update_dict = update_data.model_dump(exclude_unset=True, by_alias=True)

        update_dict["teacher"]["_id"] = ObjectId(update_dict["teacher"]["_id"])
        updated = db["class"].update_one({"_id": ObjectId(id)}, {"$set": update_dict})
        class_ = get_one(id)
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
