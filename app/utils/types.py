from pydantic import BeforeValidator
from typing import Annotated
from bson import ObjectId


def validate_object_id(value):
    if not isinstance(value, ObjectId):
        raise TypeError("ObjectId required")
    return str(value)


PyObjectId = Annotated[str, BeforeValidator(validate_object_id)]
