from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models.countries, schemas.countries, services.countries

router = APIRouter(
    prefix="/countries",
    tags=["Countries"]
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
    genres = db.query(models.countries.Countries).all()
    return genres

#Create asosiation
@router.post("/create")
def create_country(genres: schemas.countries.CountryCreate, db: Session = Depends(get_db)):
    return services.countries.create_country(db, genres)