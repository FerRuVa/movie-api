from sqlalchemy.orm import Session
import models.comments, schemas.comments

def get_comments(db: Session):
    return db.query(models.comments.Comments).all()

def create_comment(db: Session, comment: schemas.comments.CommentCreate):
    db_comment = models.comments.Comments(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment(db: Session, movie_id: int, movie: schemas.movies.MovieUpdate):
    db_movie = db.query(models.movies.Movies).filter(models.movies.Movies.id == movie_id).first()
    update_data = movie.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_movie, key, value)

    db.commit()
    db.refresh(db_movie)

    return db_movie