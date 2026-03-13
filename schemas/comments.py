from pydantic import BaseModel
from typing import Optional
from datetime import date

class CommentBase(BaseModel):
    user_id: int
    movie_id: int
    comment: str
    created_at: date

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class CommentUpdate(BaseModel):
    user_id: Optional[int]= None
    movie_id: Optional[int]= None
    comment: Optional[str]= None
    created_at: Optional[date]= None



