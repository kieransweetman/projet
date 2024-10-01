from config.database import Database
from utils.common import COLLECTION
from bson import ObjectId

from schemas.class_base import (
    ClassCollection,
    ClassBase,
    ClassCreate,
    ClassUpdate,
)


db = Database().get_db()
collection = Database().get_db().get_collection(COLLECTION.CLASS.value)


def get_all() -> ClassCollection:
    class_ = ClassCollection(classes=collection.find().to_list())

    return class_


def new(class_: ClassCreate) -> ClassBase:
    model = class_.model_dump(by_alias=True, exclude=["id"])
    model["teacher"]["_id"] = ObjectId(class_.teacher.id)
    new_id = collection.insert_one(model).inserted_id
    created_class = collection.find_one({"_id": new_id})

    return created_class

def get_one(id: str) -> ClassBase:
    class_ = collection.find_one({"_id": ObjectId(id)})
    # teacher = collection.find_one({"_id": ObjectId(class_.teacher.id)})
    
    return class_