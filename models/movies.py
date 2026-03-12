from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from time import time
from database import Base

class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    release_year = Column(Integer)
    duration = Column(Time, default=time)
    country_id = Column(Integer, ForeignKey("countries.id"), primary_key=True)
    poster_url = Column(String)
    video_url = Column(String)
    created_at = Column(DateTime, default= datetime.utcnow)

    gender = relationship("Genres", secondary="movie_genres", back_populates="movies")
    users_favorite = relationship("User",secondary="favorites", back_populates="favorite_movies")
    ratings = relationship("Ratings", back_populates="movie")
    comments = relationship("Comments", back_populates="movie")
    county = relationship("Country", back_populates="movie")