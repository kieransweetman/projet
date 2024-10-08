from config.database import Database
from utils.common import COLLECTION

from bson import ObjectId

from schemas.student_base import (
    StudentCollection,
    StudentBase,
    StudentCreate,
    StudentUpdate,
    EmbeddedGrade,
)


db = Database().get_db()
collection = Database().get_db().get_collection(COLLECTION.STUDENT.value)


def get_all():
    students = StudentCollection(students=collection.find().to_list())

    return students


def new(student: StudentCreate) -> StudentBase:
    model = student.model_dump(by_alias=True, exclude=["id"])
    new_id = collection.insert_one(model).inserted_id
    created_student = collection.find_one({"_id": new_id})

    return created_student


def get_one(id: str):
    student = collection.find_one({"_id": ObjectId(id)})
    return student


def get_grades(id: str):
    model = get_one(id)
    return [EmbeddedGrade(**grade) for grade in model["grades"]]


def delete(id: str):
    collection.delete_one({"_id": ObjectId(id)})


def update(id: str, data: StudentUpdate):
    model = data.model_dump(by_alias=True, exclude=["id"], exclude_none=True)
    collection.update_one({"_id": ObjectId(id)}, {"$set": model})
    return get_one(id)
