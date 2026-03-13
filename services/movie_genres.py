from sqlalchemy.orm import Session
from sqlalchemy import or_
import models.movie_genres, schemas.movie_genres

def get_movie_gender(db: Session):
    return db.query(models.movie_genres.MovieGenres).all()

def create_asosiation(db: Session, movie: schemas.movie_genres.MovieGenresCreate):
    db_asosiation = models.movie_genres.MovieGenres(**movie.dict())
    db.add(db_asosiation)
    db.commit()
    db.refresh(db_asosiation)
    return db_asosiation

