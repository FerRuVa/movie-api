from pydantic import BaseModel
from typing import Optional

class CountryBase(BaseModel):
    country: str

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True

class CountryUpdate(BaseModel):
    country: Optional[str]= None