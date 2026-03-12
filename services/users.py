from sqlalchemy.orm import Session
import models.users, schemas.users

def get_users(db: Session):
    return db.query(models.users.Users).all()

def create_user(db: Session, user: schemas.users.UserCreate):
    db_user = models.users.Users(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.users.Users).filter(models.users.Users.id == user_id).first()
    update_data = user.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user

def delete_user(db: Session, user_id:int):
    user = db.query(models.users.Users).filter(models.users.Users.id == user_id).first()
    db.delete(user)
    db.commit()
    return user
