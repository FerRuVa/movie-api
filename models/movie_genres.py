from sqlalchemy import Column, Integer
from database import Base

class MovieGenres(Base):
    __tablename__ = "movie_genres"

    movie_id = Column(Integer)
    gender_id = Column(Integer)
