from sqlalchemy import Column, Integer, Float, DateTime
from database import Base

class Ratings(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True, index= True)
    user_id = Column(Integer)
    movie_id = Column(Integer)
    rating = Column(Float)
    created_at = Column(DateTime)
