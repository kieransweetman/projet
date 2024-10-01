from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from utils.types import PyObjectId

config = ConfigDict(
    arbitrary_types_allowed=True,
    json_schema_extra={
        "example": {
            "name": "Class name",
            "teacher": {"_id": "ObjectId"},
            "students": [{"_id": "ObjectId", "name": "Student name"}],
        }
    },
)


class EmbeddedTeacher(BaseModel):
    id: PyObjectId = Field(..., alias="_id")


class EmbeddedStudent(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    name: str = Field(...)


class ClassBase(BaseModel):
    model_config = config
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(..., title="class name")
    teacher: Optional[EmbeddedTeacher] = Field(title="teacher", default=None)
    students: Optional[List[EmbeddedStudent]] = Field(title="student", default=[])


class ClassCreate(ClassBase):
    model_config = config

    pass


class ClassUpdate:
    model_config = config

    name: Optional[str] = None


class ClassCollection(BaseModel):
    classes: list[ClassBase]
