from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models.favorites, schemas.favorites, services.favorites

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"]
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
    favorites = db.query(models.favorites.Favorites).all()
    return favorites

#Create
@router.post("/create")
def create_favorite(favorite: schemas.favorites.FavoriteCreate, db: Session = Depends(get_db)):
    return services.favorites.create_favorite(db, favorite)

@router.delete("/{movie_id}/{user_id}")
def delete(movie_id: int, user_id: int, db: Session = Depends(get_db)):
    return services.favorites.delete_favorite(db, movie_id, user_id)
