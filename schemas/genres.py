from pydantic import BaseModel
from typing import Optional

class GenderBase(BaseModel):
    gender: str

class GenderCreate(GenderBase):
    pass

class Gender(GenderBase):
    id: int

    class Config:
        orm_mode = True

class GenderUpdate(BaseModel):
    gender: Optional[str]= None
