from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models.genres, schemas.genres, services.genres

router = APIRouter(
    prefix="/genres",
    tags=["Genres"]
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
    genres = db.query(models.genres.Genres).all()
    return genres

#Create
@router.post("/create")
def create_genred(genres: schemas.genres.GenderCreate, db: Session = Depends(get_db)):
    return services.genres.create_genred(db, genres)