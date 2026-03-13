from pydantic import BaseModel
from typing import Optional
from datetime import date


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    role: str
    create_at: date

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional [str] = None
    password: Optional [str] = None
    role: Optional [str] = None
    create_at: Optional [date] = None