from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models.movies, schemas.movies, services.movies

router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Read all
@router.get("/")
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(models.movies.Movies).all()
    return movies

#Create
@router.post("/create")
def create_movie(movie: schemas.movies.MovieCreate, db: Session = Depends(get_db)):
    return services.movies.create_movies(db, movie)

#Update
@router.patch("/update/{movie_id}")
def update_movie(movie_id: int, movie: schemas.movies.MovieUpdate, db: Session = Depends(get_db)):
    return services.movies.update_movie(db, movie_id, movie)