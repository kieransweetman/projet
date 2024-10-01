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
)

from controllers.class_controller import get_all, get_one, new


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
    id: str, update_data: ClassUpdate, db: PyMongoDatabase = Depends(Database.get_db)
):
    try:
        print(update_data)
        update_dict = update_data.model_dump(exclude_unset=True)
        print(update_dict)
        updated = db["class"].update_one({"_id": ObjectId(id)}, {"$set": update_dict})
        print(updated)
        class_ = get_one(id)
        print(class_)
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

