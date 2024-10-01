from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from utils.types import PyObjectId

config = ConfigDict(
    arbitrary_types_allowed=True, json_schema_extra={"example": {"name": "Mathematics"}}
)


class SubjectBase(BaseModel):
    model_config = config

    id: PyObjectId = Field(default=None, alias="_id")
    original_id: Optional[int] = Field(default=None, title="original id")
    name: str


class SubjectCreate(SubjectBase):
    model_config = config
    pass


class SubjectUpdate:
    name: Optional[str] = None
