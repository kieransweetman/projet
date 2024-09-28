from pydantic import BaseModel, Field, BeforeValidator
from typing import Optional, Annotated
from bson import ObjectId


class StudentBase(BaseModel):
    nom: str = Field(..., title="Nom de l'élève")
    prenom: str = Field(..., title="Prénom de l'élève")
    age: int = Field(..., title="Age de l'élève")
    sexe: str = Field(..., title="Sexe de l'élève")
    classe: str = Field(..., title="Classe de l'élève")
    adresse: str = Field(..., title="Adresse de l'élève")


PyObjectId = Annotated[str, BeforeValidator(str)]


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    nom: Optional[str]
    prenom: Optional[str]
    age: Optional[int]
    sexe: Optional[str]
    # classe: Optional[str]
    adresse: Optional[str]


class Student(StudentBase):
    id: str = Field(ObjectId, title="ID de l'élève", alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
