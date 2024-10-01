from bson import ObjectId
from config.database import Database
from utils.common import COLLECTION

from schemas.teacher_base import (
    TeacherBase,
    TeacherCreate,
    TeacherCollection,
)


db = Database().get_db()
collection = Database().get_db().get_collection(COLLECTION.TEACHER.value)


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