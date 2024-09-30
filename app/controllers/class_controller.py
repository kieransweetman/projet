from config.database import Database
from utils.common import COLLECTION

from schemas.class_base import (
    ClassCollection,
    ClassBase,
    ClassCreate,
)


db = Database().get_db()
collection = Database().get_db().get_collection(COLLECTION.CLASS.value)


def get_all() -> ClassCollection:
    class_ = ClassCollection(classes=collection.find().to_list())

    return class_


def new(class_: ClassCreate) -> ClassBase:
    model = class_.model_dump(by_alias=True, exclude=["id"])
    new_id = collection.insert_one(model).inserted_id
    created_class = collection.find_one({"_id": new_id})

    return created_class
