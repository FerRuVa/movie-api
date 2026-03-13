from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
class Comments(Base):
    __tablename__ = "comments"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("Users", back_populates="comments")
    movie = relationship("Movies", back_populates="comments")