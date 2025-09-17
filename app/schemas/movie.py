from pydantic import BaseModel
from typing import Optional

class MovieBase(BaseModel):
    tconst: str
    primarytitle: str
    genres: Optional[str]

class MovieDetail(MovieBase):
    averagerating: Optional[float]
    numvotes: Optional[int]

class Recommendation(BaseModel):
    tconst: str
    title: str
    score: float
