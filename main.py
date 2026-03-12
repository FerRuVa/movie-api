from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependencia de la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

