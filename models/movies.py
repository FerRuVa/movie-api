from sqlalchemy import Column, Integer, String, DateTime, Time
from database import Base

class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    release_year = Column(Integer)
    duration = Column(Time)
    country_id = Column(Integer)
    gender_id = Column(Integer)
    poster_url = Column(String)
    video_url = Column(String)
    created_at = Column(DateTime)