from config.database import Database
from schemas.student_base import StudentBase, StudentUpdate, StudentCreate
from bson import ObjectId, json_util
from datetime import datetime


student_collection = Database().get_db().get_collection("student")


def get_all_students():
    data = student_collection.find().to_list()

    return [StudentBase(**student) for student in data]


def by_id(id: str):
    data = student_collection.find_one({"_id": ObjectId(id)})
    return StudentBase(**data)


def delete_student(id: str):
    student_collection.delete_one({"_id": ObjectId(id)})


def create(student: StudentCreate):

    model = student.model_dump()
    new_student = student_collection.insert_one(model)

    created = student_collection.find_one({"_id": new_student.inserted_id})
    return created


def update(student: StudentUpdate, id: str):
    student_collection.update_one(
        {"_id": id}, {"$set": student.model_dump(exclude_unset=True)}
    )
    return student_collection.find_one({"_id": student.id})
