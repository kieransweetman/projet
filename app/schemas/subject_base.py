from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


config = ConfigDict(
    arbitrary_types_allowed=True, json_schema_extra={"example": {"name": "Mathematics"}}
)


class SubjectBase(BaseModel):
    model_config = config
    name: str


class SubjectCreate(SubjectBase):
    model_config = config
    pass


class SubjectUpdate:
    name: Optional[str] = None
