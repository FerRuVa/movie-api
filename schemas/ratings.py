from pydantic import BaseModel
from typing import Optional
from datetime import date

class RatingBase(BaseModel):
    user_id = int
    movie_id = int
    rating = float
    created_at = date

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int

    class Config:
        orm_mode = True

class RatingUpdate(BaseModel):
    user_id = Optional[int]= None
    movie_id = Optional[int]= None
    rating = Optional[float]= None
    created_at = Optional[date]= None