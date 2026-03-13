from pydantic import BaseModel
from typing import Optional

class CountryBase(BaseModel):
    country: str

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class CountryUpdate(BaseModel):
    country: Optional[str]= None