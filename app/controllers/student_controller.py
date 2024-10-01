from config.database import Database
from utils.common import COLLECTION

from bson import ObjectId

from schemas.student_base import (
    StudentCollection,
    StudentBase,
    StudentCreate,
)


db = Database().get_db()
collection = Database().get_db().get_collection(COLLECTION.STUDENT.value)


def get_all() -> StudentCollection:
    students = StudentCollection(students=collection.find().to_list())

    return students


def new(student: StudentCreate) -> StudentBase:
    model = student.model_dump(by_alias=True, exclude=["id"])
    new_id = collection.insert_one(model).inserted_id
    created_student = collection.find_one({"_id": new_id})

    return created_student


def get_one(id: str) -> StudentBase:
    student = collection.find_one({"_id": ObjectId(id)})

    return student


def get_grades(id: str):
    student = StudentBase(**collection.find_one({"_id": ObjectId(id)}))

    return student.grades
