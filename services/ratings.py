from sqlalchemy.orm import Session
import models.ratings, schemas.ratings

def get_ratings(db: Session):
    return db.query(models.ratings.Ratings).all()

def create_rating(db: Session, rating: schemas.ratings.RatingCreate):
    db_rating = models.ratings.Ratings(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
