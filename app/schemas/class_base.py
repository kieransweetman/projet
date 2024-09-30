from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from utils.types import PyObjectId

config = ConfigDict(
    arbitrary_types_allowed=True,
    json_schema_extra={
        "example": {
            "name": "Class name"
        }
    }
)

class EmbeddedTeacher:
    id: PyObjectId=Field(...,alias="_id")

class EmbeddedStudent:
    id: PyObjectId=Field(...,alias="_id")

class ClassBase(BaseModel):
    model_config = config
    name: str
    teacher: Optional[EmbeddedTeacher]
    student: Optional[EmbeddedStudent]

class ClassCreate(ClassBase):
    pass


class ClassUpdate():
    name:Optional[str] = None