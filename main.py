from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database import engine, Base
import models

from routers import users_router, ratings_router, movies_router, genres_router, favorites_router, countries_router, comments_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Movies API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router.router)
app.include_router(ratings_router.router)
app.include_router(movies_router.router)
app.include_router(genres_router.router)
app.include_router(favorites_router.router)
app.include_router(countries_router.router)
app.include_router(comments_router.router)