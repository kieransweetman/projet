from bson import ObjectId
from config.database import Database
from utils.common import COLLECTION

from schemas.teacher_base import (
    TeacherBase,
    TeacherCreate,
    TeacherCollection,
    TeacherUpdate,
)


db = Database().get_db()
collection = db.get_collection(COLLECTION.TEACHER.value)
class_collection = db.get_collection(COLLECTION.CLASS.value)


def get_all() -> TeacherCollection:
    teachers = TeacherCollection(teachers=collection.find().to_list())

    return teachers


def new(teacher: TeacherCreate) -> TeacherBase:
    model = teacher.model_dump(by_alias=True, exclude=["id"])
    new_id = collection.insert_one(model).inserted_id
    created_teacher = collection.find_one({"_id": new_id})

    return created_teacher


def get_one(id: str) -> TeacherBase:
    teacher = collection.find_one({"_id": ObjectId(id)})

    return teacher


def delete(id: str):
    collection.delete_one({"_id": ObjectId(id)})


def teachers_students(teacher_id: str):
    classes = class_collection.find({"teacher._id": ObjectId(teacher_id)}).to_list()
    students = [s for c in classes for s in c["students"]]
    return students


def update(id: str, data: TeacherUpdate):
    model = data.model_dump(by_alias=True, exclude=["id"], exclude_none=True)
    collection.update_one({"_id": ObjectId(id)}, {"$set": model})
    return get_one(id)
