from pydantic import ConfigDict, Field
from .person_base import PersonBase, PersonCreate, PersonUpdate
from typing import Optional, List
from pydantic import BaseModel
from utils.types import PyObjectId


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


class EmbeddedClass(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)


class TeacherBase(PersonBase):
    classes: List[EmbeddedClass] = []
    model_config = config


class TeacherCreate(PersonCreate):
    model_config = config
    pass


class TeacherUpdate(PersonUpdate):
    model_config = config
    pass


class TeacherCollection(BaseModel):
    teachers: List[TeacherBase]
