from typing import Optional
from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, field_serializer, field_validator
from utils.types import PyObjectId

config = ConfigDict(
    arbitrary_types_allowed=True,
    json_schema_extra={"example": {"name": "TRIM", "date": "2000-01-01"}},
)


class TrimesterBase(BaseModel):
    model_config = config
    id: PyObjectId = Field(default=None, alias="_id")
    name: str = Field(..., title="trimester name")
    date: datetime = Field(..., title="trimester date")
    original_id: Optional[int] = Field(title="original id", default=None)

    @field_validator("date", mode="before")
    def parse_date(cls, value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value

    @field_serializer("date")
    def serialize_date(self, date: datetime, _info):
        return date.replace(tzinfo=None).isoformat()

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        data["date"] = self.date
        return data


class TrimesterCreate(TrimesterBase):
    model_config = config

    pass


class TrimesterUpdate:
    model_config = config

    name: Optional[str] = None
    date: Optional[datetime] = None
