from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Trade(BaseModel):
    id: int
    sum: int = Field(gt=0, default=1)
    discount: int = Field(ge=0, le=100, default=0)


class Pydantic_User(BaseModel):
    id: int
    username: str
