from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from utils.types import PyObjectId

config = ConfigDict(
    arbitrary_types_allowed=True,
    json_schema_extra={
        "example": {"name": "Class name", "teacher": {"_id": "ObjectId"}}
    },
)


class EmbeddedTeacher(BaseModel):
    id: PyObjectId = Field(..., alias="_id")


class EmbeddedStudent(BaseModel):
    id: PyObjectId = Field(..., alias="_id")


class ClassBase(BaseModel):
    model_config = config
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(..., title="class name")
    teacher: Optional[EmbeddedTeacher] = Field(title="teacher", default=None)
    student: Optional[EmbeddedStudent] = Field(title="student", default=None)


class ClassCreate(ClassBase):
    pass


class ClassUpdate:
    name: Optional[str] = None


class ClassCollection(BaseModel):
    classes: list[ClassBase]
