from sqlalchemy import Column, Integer, String
from database import Base

class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key = True, index= True)
    gender = Column(String)