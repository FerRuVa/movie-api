from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index= True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String)
    create_at = Column(DateTime)

    favorite_movies = relationship("Movie", secondary="favorites", back_populates="users_favorite")
    ratings = relationship("Ratings", back_populates="user")
    comments = relationship("Comments", back_populates="user")