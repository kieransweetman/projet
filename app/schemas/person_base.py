from pydantic import BaseModel, Field, ConfigDict, field_serializer, field_validator
from typing import Optional, List
from utils.types import PyObjectId
from datetime import datetime


class PersonBase(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    last_name: str = Field(..., title="student last name")
    name: str = Field(..., title="student first name")
    birth_date: datetime = Field(..., title="Date of birth")
    sex: str = Field(..., title="student sex type")
    address: str = Field(..., title="student's address")
    original_id: Optional[int] = Field(default=None, title="csv original id")

    @field_validator("birth_date", mode="before")
    def parse_birth_date(cls, value):
        if isinstance(value, str):
            return datetime.fromisoformat(value).replace(tzinfo=None)
        return value

    @field_serializer("birth_date")
    def serialize_birth_date(self, birth_date: datetime, _info):
        if birth_date is None:
            return None
        return birth_date.replace(tzinfo=None).isoformat()

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        if "birth_date" in data and data["birth_date"] is not None:
            data["birth_date"] = self.birth_date
        return data


class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonBase):
    last_name: Optional[str] = None
    name: Optional[str] = None
    birth_date: Optional[datetime] = None
    sex: Optional[str] = None
    classe: Optional[str] = None
    address: Optional[str] = None
