from sqlalchemy.orm import Session
import models.favorites, schemas.favorites

def get_favorites(db: Session):
    return db.query(models.favorites.Favorites).all()

def create_favorite(db: Session, rating: schemas.favorites.FavoriteCreate):
    db_rating = models.favorites.Favorites(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def delete_favorite(db: Session, movie_id: int, user_id: int):
    favorite= db.query(models.favorites.Favorites).filter(models.favorites.Favorites.user_id == user_id & models.favorites.Favorites.movie_id == movie_id)
    db.delete(favorite)
    db.commit()
    return favorite