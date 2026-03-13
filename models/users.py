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

    favorites = relationship("Favorites", back_populates="user")
    ratings = relationship("Ratings", back_populates="user")
    comments = relationship("Comments", back_populates="user")