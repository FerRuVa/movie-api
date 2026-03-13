from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models.ratings, schemas.ratings, services.ratings

router = APIRouter(
    prefix="/ratings",
    tags=["Ratings"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#Read all
@router.get("/")
def get_ratings(db: Session = Depends(get_db)):
    ratings = db.query(models.ratings.Ratings).all()
    return ratings

#Create user
@router.post("/create")
def create_rating(user: schemas.ratings.RatingCreate, db: Session = Depends(get_db)):
    return services.ratings.create_rating(db, user)