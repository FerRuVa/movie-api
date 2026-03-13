from pydantic import BaseModel
from typing import Optional

class FavoriteBase(BaseModel):
    user_id: int
    movie_id: int

class FavoriteCreate(FavoriteBase):
    pass

class Favorite(FavoriteBase):

    model_config = {
        "from_attributes": True
    }

class FavoriteUpdate(BaseModel):
    user_id: Optional[int]= None
    movie_id: Optional[int]= None