from config.database import Database
from pymongo.collection import Collection
from schemas.teacher_base import TeacherBase, TeacherUpdate
from bson import ObjectId

teacher_collection = Database().get_db().get_collection("teacher")


def get_all_teachers():
    data = teacher_collection.find().to_list()

    return [TeacherBase(**teacher) for teacher in data]


def by_id(id: str):
    data = teacher_collection.find_one({"_id": ObjectId(id)})
    return TeacherBase(**data)


def delete_teacher(id: str):
    teacher_collection.delete_one({"_id": ObjectId(id)})


def create(teacher: TeacherBase):
    new_teacher = teacher_collection.insert_one(teacher.model_dump())

    created = teacher_collection.find_one({"_id": new_teacher.inserted_id})
    return created


def update(teacher: TeacherUpdate, id: str):
    teacher_collection.update_one(
        {"_id": id}, {"$set": teacher.model_dump(exclude_unset=True)}
    )
    return teacher_collection.find_one({"_id": teacher.id})
