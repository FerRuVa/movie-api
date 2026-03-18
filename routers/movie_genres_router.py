from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models.movie_genres, schemas.movie_genres, services.movie_genres

router = APIRouter(
    prefix="/movie_genres",
    tags=["MovieGenres"]
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
    genres = db.query(models.movie_genres.MovieGenres).all()
    return genres

#Create asosiation
@router.post("/create")
def create_asotiation(genres: schemas.movie_genres.MovieGenresCreate, db: Session = Depends(get_db)):
    return services.movie_genres.create_asosiation(db, genres)