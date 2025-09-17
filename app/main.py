from fastapi import FastAPI
from app.api import movies, recommendations
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="IMDb Movie Recommendation API")

origins = [
    "http://localhost:5011",  # React dev server default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(movies.router, prefix="/api/movies", tags=["movies"])
app.include_router(recommendations.router, prefix="/api/recommendations", tags=["recommendations"])
