from sqlalchemy import Column, Integer
from database import Base

class Favorites(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key = True, index= True)
    user_id = Column(Integer)
    movie_id = Column(Integer)