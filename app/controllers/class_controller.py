from config.database import Database
from utils.common import COLLECTION
from bson import ObjectId
from typing import List

from schemas.class_base import ClassCollection, ClassBase, ClassCreate, EmbeddedStudent


db = Database().get_db()
collection = Database().get_db().get_collection(COLLECTION.CLASS.value)


def get_all() -> ClassCollection:
    class_list = collection.find().to_list()
    class_collection = ClassCollection(classes=class_list)

    return class_collection


def new(class_: ClassCreate) -> ClassBase:
    model = class_.model_dump(by_alias=True, exclude=["id"])
    model["teacher"]["_id"] = ObjectId(class_.teacher.id)
    new_id = collection.insert_one(model).inserted_id
    created_class = collection.find_one({"_id": new_id})

    return created_class


def add_student(class_id: str, students: List[EmbeddedStudent]) -> ClassBase:
    class_model = collection.find_one({"_id": ObjectId(class_id)})
    c = ClassBase(**class_model)
    for student in students:
        c.students.append(student)

    dumped = c.model_dump(by_alias=True, exclude=["id"])

    print("dumping\n###\n", dumped)
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
    print(class_)
    return class_.students
