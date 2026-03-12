from sqlalchemy.orm import Session
import models.ratings, schemas.ratings

def get_ratings(db: Session):
    return db.query(models.ratings.Ratings).all()

