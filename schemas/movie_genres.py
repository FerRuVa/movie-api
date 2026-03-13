from pydantic import BaseModel
from typing import Optional

class MovieGenresBase(BaseModel):
    movie_id: int
    gender_id: int

class MovieGenresCreate(MovieGenresBase):
    pass

class MovieGenres(MovieGenresBase):
    model_config = {
        "from_attributes": True
    }