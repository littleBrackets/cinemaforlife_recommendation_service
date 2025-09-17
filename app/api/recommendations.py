from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.crud.movie import get_top_movies
from app.recommender.content_based import ContentBasedRecommender
from app.schemas.movie import Recommendation

router = APIRouter()

@router.get("/", response_model=list[Recommendation])
async def get_recommendations(title: str, db: AsyncSession = Depends(get_db)):
    records = await get_top_movies(db, limit=1000)
    movies = [movie for movie, _ in records]

    recommender = ContentBasedRecommender(movies)
    recommendations = recommender.recommend(title, top_n=5)
    if not recommendations:
        raise HTTPException(status_code=404, detail="Movie not found or no recommendations")

    return [
        Recommendation(tconst=tconst, title=title, score=score)
        for tconst, title, score in recommendations
    ]
