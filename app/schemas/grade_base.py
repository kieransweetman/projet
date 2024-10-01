from pydantic import BaseModel, Field, ConfigDict, field_serializer, field_validator
from typing import Optional, List
from utils.types import PyObjectId
from datetime import datetime


class GradeBase(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    date_entered: datetime = Field(..., title="Date of grade")
    value: float = Field(..., title="Grade value")
    # student: PyObjectId = Field(..., title="Student id")
    # class: PyObjectId = Field(..., title="Class id")
    # subject: PyObjectId = Field(..., title="Subject id")
    advancement: float = Field(..., title="Advancement value")
    opinion: str = Field(..., title="Teacher opinion")

    @field_validator("date_entered", mode="before")
    def parse_date_entered(cls, value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value

    @field_serializer("date_entered")
    def serialize_date_entered(self, date_entered: datetime, _info):
        return date_entered.replace(tzinfo=None).isoformat()

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        data["date_entered"] = self.date_entered
        return data


class GradeCreate(GradeBase):
    pass


class GradeUpdate(GradeBase):
    date_entered: Optional[datetime]
    value: Optional[float]
    # student: Optional[PyObjectId]
    # subject: Optional[PyObjectId]
    advancement: Optional[float]
    opinion: Optional[str]
