from typing import List
from fastapi import APIRouter, HTTPException, status, Body


from config.database import Database
from pymongo.database import Database as PyMongoDatabase

from schemas.class_base import (
    ClassCollection,
    ClassBase,
    ClassCreate,
    ClassUpdate,
)

from controllers.class_controller import get_all, new


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
