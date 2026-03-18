from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models.comments, schemas.comments, services.comments

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
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
    comment = db.query(models.comments.Comments).all()
    return comment

#Create
@router.post("/create")
def create_comment(comment: schemas.comments.CommentCreate, db: Session = Depends(get_db)):
    return services.comments.create_comment(db, comment)

@router.patch("/update/{movie_id}/{user_id}")
def update_comment(movie_id: int, user_id: int, comment: schemas.comments.CommentUpdate, db: Session = Depends(get_db)):
    return services.comments.update_comment(db, movie_id, user_id, comment)