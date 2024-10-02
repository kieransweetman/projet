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
                    "trimester": {
                        "name": "first",
                    },
                },
            ],
        }
    },
)


class EmbbededTrimester(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)


class EmbeddedGrade(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    subject: str = Field(...)
    value: float = Field(...)
    trimester: EmbbededTrimester = Field(..., title="trimester")


class StudentBase(PersonBase):
    model_config = config
    grades: Optional[List[EmbeddedGrade]] = []
    pass


class StudentCreate(PersonCreate):
    model_config = config
    grades: Optional[List[EmbeddedGrade]] = []
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
