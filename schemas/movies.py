from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class MovieBase(BaseModel):
    title = str
    description = str
    release_year = int
    duration = time
    country_id = int
    gender_id = int
    poster_url = str
    video_url = str
    created_at = date

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True

class MovieUpdate(BaseModel):
    title = Optional[str]= None
    description = Optional[str] = None
    release_year = Optional[int]= None
    duration = Optional[time] = None
    country_id = Optional[int]= None
    gender_id = Optional[int]= None
    poster_url = Optional[str] = None
    video_url = Optional[str] = None
    created_at = Optional[date] = None