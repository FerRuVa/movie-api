from sqlalchemy.orm import Session
import models.countries, schemas.countries

def get_countries(db: Session):
    return db.query(models.countries.Countries).all()

def create_country(db: Session, country: schemas.countries.CountryCreate):
    db_country = models.countries.Countries(**country.dict())
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country