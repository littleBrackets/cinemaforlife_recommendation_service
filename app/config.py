from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost/imdb"
    user_service_url: str = "https://userservice.example.com/api/validate-token"

    class Config:
        env_file = ".env"

settings = Settings()
