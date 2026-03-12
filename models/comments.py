from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Comments(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key = True, index= True)
    user_id = Column(Integer)
    movie_id = Column(Integer)
    comment = Column(String)
    created_at = Column(DateTime)