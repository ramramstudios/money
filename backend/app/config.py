from pydantic_settings import BaseSettings

from pydantic import BaseSettings

class Settings(BaseSettings):
    MARKET_API_KEY: str = ""
    DATABASE_URL: str = "sqlite:///./app.db"
    REDIS_URL: str = "redis://redis:6379"

settings = Settings(_env_file=".env")
