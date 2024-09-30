from pydantic import BaseModel, Field, ConfigDict, field_serializer, field_validator
from typing import Optional, List
from utils.types import PyObjectId
from datetime import datetime
from bson import json_util


config = ConfigDict(
    arbitrary_types_allowed=True,
    json_schema_extra={
        "example": {
            "nom": "Doe",
            "prenom": "John",
            "email": "jdoe@example.com",
            "date_naissance": "2000-01-01T00:00:00",
            "sexe": "M",
            "adresse": "123 rue sesame",
        }
    },
)


class StudentBase(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    nom: str = Field(..., title="Nom de l'élève")
    prenom: str = Field(..., title="Prénom de l'élève")
    date_naissance: datetime = Field(..., title="Date de naissacnce")
    sexe: str = Field(..., title="Sexe de l'élève")
    adresse: str = Field(..., title="Adresse de l'élève")
    original_id: Optional[int] = Field(default=None, title="ID original de l'élève")

    model_config = config

    @field_validator("date_naissance", mode="before")
    def parse_date_naissance(cls, value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value

    @field_serializer("date_naissance")
    def serialize_date_naissance(self, date_naissance: datetime, _info):
        return date_naissance.isoformat(timespec="seconds")

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        data["date_naissance"] = self.date_naissance
        return data


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    nom: Optional[str]
    prenom: Optional[str]
    date_naissance: Optional[int]
    sexe: Optional[str]
    classe: Optional[str]
    adresse: Optional[str]


class StudentCollection(BaseModel):
    students: List[StudentBase]
