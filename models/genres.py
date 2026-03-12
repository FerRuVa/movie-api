from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key = True, index= True)
    gender = Column(String)

    movies = relationship("Movie", secondary="movie_genres", back_populates="genres")