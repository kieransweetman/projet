from pydantic import ConfigDict
from .person_base import PersonBase, PersonCreate, PersonUpdate
from typing import Optional, List
from pydantic import BaseModel


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


class TeacherBase(PersonBase):
    model_config = config


class TeacherCreate(PersonCreate):
    pass


class TeacherUpdate(PersonUpdate):
    pass


class TeacherCollection(BaseModel):
    teachers: List[TeacherBase]
