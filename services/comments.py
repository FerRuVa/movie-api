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

def update_comment(db: Session, movie_id: int, user_id: int, comment: schemas.comments.CommentUpdate):
    db_comment = db.query(models.comments.Comments).filter(models.comments.Comments.movie_id == movie_id & models.comments.Comments.user_id == user_id).first()
    update_data = comment.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_comment, key, value)

    db.commit()
    db.refresh(db_comment)

    return db_comment