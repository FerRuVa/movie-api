from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Countries(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key = True, index= True)
    country = Column(String)

    movies = relationship("Movies", back_populates="country")