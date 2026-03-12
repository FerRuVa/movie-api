from fastapi import FastAPI
from database import engine, Base
import models

#from routers import movie_router, user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Movies API"
)