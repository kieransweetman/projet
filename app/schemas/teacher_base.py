from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from utils.types import PyObjectId
from datetime import datetime


class TeacherBase(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    nom: str = Field(..., title="Nom de l'élève")
    prenom: str = Field(..., title="Prénom de l'élève")
    date_naissace: datetime = Field(..., title="Age de l'élève")
    sexe: str = Field(..., title="Sexe de l'élève")
    adresse: str = Field(..., title="Adresse de l'élève")
    original_id: Optional[int] = Field(..., title="ID original de l'élève")
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "nom": "Doe",
                "prenom": "John",
                "email": "jdoe@example.com",
                "date_naissance": "2000-01-01",
                "sexe": "M",
                "adresse": "123 rue sesame",
            }
        },
    )


class TeacherCreate(TeacherBase):
    pass


class TeacherUpdate(BaseModel):
    nom: Optional[str]
    prenom: Optional[str]
    date_naissance: Optional[int]
    sexe: Optional[str]
    adresse: Optional[str]
