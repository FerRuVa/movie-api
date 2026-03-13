from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models.users, schemas.users, services.users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#Read all
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.users.Users).all()
    return users

#Create user
@router.post("/create")
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    return services.users.create_user(db, user)

#Update user
@router.patch("/update/{user_id}")
def update_user(user_id: int, user: schemas.users.UserUpdate, db: Session = Depends(get_db)):
    return services.users.update_user(db, user_id, user)

#delete
@router.delete('/{user_id}')
def delete_user(user_id: int, user: schemas.users.UserUpdate, db: Session = Depends(get_db)):
    return services.users.delete_user(db, user_id, user)