from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.movie import TitleBasics, TitleRatings

async def get_movie(db: AsyncSession, tconst: str):
    result = await db.execute(select(TitleBasics).where(TitleBasics.tconst==tconst))
    movie = result.scalars().first()
    return movie

async def get_movie_with_rating(db: AsyncSession, tconst: str):
    stmt = select(TitleBasics, TitleRatings).join(TitleRatings, TitleBasics.tconst==TitleRatings.tconst).where(TitleBasics.tconst == tconst)
    result = await db.execute(stmt)
    record = result.first()
    if record:
        movie, rating = record
        return movie, rating
    return None, None

async def get_top_movies(db: AsyncSession, limit: int = 10):
    stmt = select(TitleBasics, TitleRatings).join(TitleRatings, TitleBasics.tconst==TitleRatings.tconst).order_by(TitleRatings.averagerating.desc()).limit(limit)
    result = await db.execute(stmt)
    return result.all()
