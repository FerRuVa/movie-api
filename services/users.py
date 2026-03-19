from sqlalchemy.orm import Session
from core.security import hash_password, verify_password
import models.users, schemas.users

def get_users(db: Session):
    return db.query(models.users.Users).all()

def create_user(db: Session, user: schemas.users.UserCreate):
    print("Password:", user.password)
    print("Length:", len(user.password))
    hashed_password = hash_password(user.password)
    print("Password:", hashed_password)
    print("Length:", len(hashed_password))
    db_user = models.users.Users(
        username = user.username,
        email = user.email,
        password = hashed_password,
        role = user.role,
        create_at = user.create_at
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.users.Users).filter(models.users.Users.id == user_id).first()
    update_data = user.model_dump(exclude_unset=True)
    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])
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

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.users.Users).filter(models.users.Users.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user