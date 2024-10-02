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
            "grades": [
                {
                    "subject": "math",
                    "value": "A",
                    "trimester": {},
                },
            ],
        }
    },
)


class EmbbededTrimester(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)


class EmbeddedGrade(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    subject: Optional[str] = Field(default=None)
    value: Optional[float] = Field(default=None)
    trimester: Optional[EmbbededTrimester] = Field(title="trimester", default=None)


class StudentBase(PersonBase):
    model_config = config
    grades: Optional[List[EmbeddedGrade]] = Field(default_factory=list)
    pass


class StudentCreate(PersonCreate):
    model_config = config
    grades: Optional[List[EmbeddedGrade]] = Field(default_factory=list)
    origin_class_id: int = None

    pass


class StudentUpdate(PersonUpdate):
    model_config = config

    last_name: Optional[str] = None
    name: Optional[str] = None
    birth_date: Optional[int] = None
    sex: Optional[str] = None
    classe: Optional[str] = None
    address: Optional[str] = None
    grades: Optional[List[EmbeddedGrade]] = None


class StudentCollection(BaseModel):
    students: List[StudentBase]
