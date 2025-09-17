from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.movie import get_top_movies, get_movie_with_rating
from app.schemas.movie import MovieDetail
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=list[MovieDetail])
async def top_movies(limit: int = 10, db: AsyncSession = Depends(get_db)):
    records = await get_top_movies(db, limit)
    movies = []
    for movie, rating in records:
        movies.append(
            MovieDetail(
                tconst=movie.tconst,
                primarytitle=movie.primarytitle,
                genres=movie.genres,
                averagerating=rating.averagerating,
                numvotes=rating.numvotes,
            )
        )
    return movies

@router.get("/{tconst}", response_model=MovieDetail)
async def movie_detail(tconst: str, db: AsyncSession = Depends(get_db)):
    movie, rating = await get_movie_with_rating(db, tconst)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return MovieDetail(
        tconst=movie.tconst,
        primarytitle=movie.primarytitle,
        genres=movie.genres,
        averagerating=rating.averagerating if rating else None,
        numvotes=rating.numvotes if rating else None,
    )
