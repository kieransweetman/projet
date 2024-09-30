from typing import Optional
from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime

config = ConfigDict(
    arbitrary_types_allowed=True,
    json_schema_extra={
        "example": {
            "name": "TRIM",
            "date": "2000-01-01"
        }
    }
)

class TrimesterBase(BaseModel):
    model_config = config
    name: str
    date: datetime


class TrimesterCreate(TrimesterBase):
    pass


class TrimesterUpdate():
    name:Optional[str] = None
    date:Optional[datetime] = None