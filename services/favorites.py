from sqlalchemy.orm import Session
import models.favorites, schemas.favorites


def get_favorites(db: Session):
    return db.query(models.favorites.Favorites).all()


def create_favorite(db: Session, favorite: schemas.favorites.FavoriteCreate):

    db_favorite = models.favorites.Favorites(**favorite.dict())

    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)

    return db_favorite


def delete_favorite(db: Session, movie_id: int, user_id: int):

    favorite = db.query(models.favorites.Favorites).filter(
        models.favorites.Favorites.user_id == user_id,
        models.favorites.Favorites.movie_id == movie_id
    ).first()

    if not favorite:
        return None

    db.delete(favorite)
    db.commit()

    return favorite