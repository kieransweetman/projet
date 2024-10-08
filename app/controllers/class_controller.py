from config.database import Database
from utils.common import COLLECTION
from bson import ObjectId
from typing import List

from schemas.class_base import ClassCollection, ClassBase, ClassCreate, EmbeddedStudent


db = Database().get_db()
collection = Database().get_db().get_collection(COLLECTION.CLASS.value)


def get_all() -> ClassCollection:
    class_ = ClassCollection(classes=collection.find().to_list())

    return class_


def new(class_: ClassCreate) -> ClassBase:
    model = class_.model_dump(by_alias=True, exclude=["id"], exclude_none=True)
    print(model)
    new_id = collection.insert_one(model).inserted_id
    created_class = collection.find_one({"_id": new_id})

    return created_class


def add_student(class_id: str, students: List[EmbeddedStudent]) -> ClassBase:
    class_model = collection.find_one({"_id": ObjectId(class_id)})
    c = ClassBase(**class_model)
    for student in students:
        if db["student"].find_one({"_id": student.id}):
            c.students.append(student)
        else:
            raise Exception(f"Student not found: {student.name} - id: {student.id}")

    dumped = c.model_dump(by_alias=True, exclude=["id"])

    dumped["teacher"]["_id"] = ObjectId(dumped["teacher"]["_id"])

    for s in dumped["students"]:
        s["_id"] = ObjectId(s["_id"])

    updated = collection.update_one(
        {"_id": ObjectId(class_id)},
        {"$set": dumped},
    )
    if updated.modified_count == 1:
        return collection.find_one({"_id": ObjectId(class_id)})
    else:
        raise Exception("Failed to update class")


def get_one(id: str):
    class_ = collection.find_one({"_id": ObjectId(id)})

    return class_


def get_students(class_id: str):
    class_ = ClassBase(**get_one(class_id))
    return class_.students
