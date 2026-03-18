from fastapi import FastAPI
from database import engine, Base
import models

from routers import users_router, ratings_router, movies_router, movie_genres_router, genres_router, favorites_router, countries_router, comments_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Movies API"
)

app.include_router(users_router.router)
app.include_router(ratings_router.router)
app.include_router(movies_router.router)
app.include_router(movie_genres_router.router)
app.include_router(genres_router.router)
app.include_router(favorites_router.router)
app.include_router(countries_router.router)
app.include_router(comments_router.router)