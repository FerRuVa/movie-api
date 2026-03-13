from sqlalchemy.orm import Session
import models.genres, schemas.genres

def get_genres(db: Session):
    return db.query(models.genres.Genres).all()

def create_genred(db: Session, genred: schemas.genres.GenderCreate):
    db_genred = models.genres.Genres(**genred.dict())
    db.add(db_genred)
    db.commit()
    db.refresh(db_genred)
    return db_genred