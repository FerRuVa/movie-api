from sqlalchemy.orm import Session
from sqlalchemy import or_
import models.movies, schemas.movies

# FILTRO DE BÚQUEDA DE TODAS LAS PELICULAS
def get_movies(db: Session):
    return db.query(models.movies.Movies).all()

# CREACIÓN DE PELICULAS
def create_movies(db: Session, movie: schemas.movies.MovieCreate):
    db_movie = models.movies.Movies(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# FILTRO DE BÚQUEDA DE PELICULAS POR NOMBRE O DESCRIPCIÓN
def get_query(db: Session, search: str | None = None):
    query = db.query(models.Movies)

    if search:
        query = query.filter(
            or_(
                models.Movies.title.ilike(f"%{search}"),
                models.Movies.description.ilike(f"%{search}")
            )
        )

    return query.all()
# FILTRO DE BÚQUEDA DE PELICULAS POR AÑO DE ESTRENO
def get_year(db: Session, year: int, movie: schemas.movies.Movie):
        return db.query(models.movies.Movies).filter(models.movies.Movies.release_year == year).first()

# ACTUALIZACIÓN DE PELICULAS
def update_movie(db: Session, movie_id: int, movie: schemas.movies.MovieUpdate):
    db_movie = db.query(models.movies.Movies).filter(models.movies.Movies.id == movie_id).first()
    update_data = movie.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_movie, key, value)

    db.commit()
    db.refresh(db_movie)

    return db_movie

# ELIMINACIÓN DE PELICULAS
def delete_movie(db: Session, movie_id: int):
    movie = db.query(models.movies.Movies).filter(models.movies.Movies.id == movie_id).first()
    db.delete(movie)
    db.commit()
    return movie
