from pydantic import BaseModel, Field, ConfigDict, field_serializer, field_validator
from .person_base import PersonBase, PersonCreate, PersonUpdate
from typing import Optional, List
from utils.types import PyObjectId
from datetime import datetime
from bson import json_util


config = ConfigDict(
    arbitrary_types_allowed=True,
    json_schema_extra={
        "example": {
            "last_name": "Doe",
            "name": "John",
            "email": "jdoe@example.com",
            "birth_date": "2000-01-01T00:00:00",
            "sex": "M",
            "address": "123 rue sesame",
        }
    },
)


class StudentBase(PersonBase):
    model_config = config
    pass


class StudentCreate(PersonCreate):
    pass


class StudentUpdate(PersonUpdate):
    last_name: Optional[str]
    name: Optional[str]
    birth_date: Optional[int]
    sex: Optional[str]
    classe: Optional[str]
    address: Optional[str]


class StudentCollection(BaseModel):
    students: List[StudentBase]
