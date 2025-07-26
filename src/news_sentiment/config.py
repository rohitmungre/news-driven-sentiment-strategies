from pydantic import BaseSettings

class Settings(BaseSettings):
    newsapi_key: str

    class Config:
        env_file = ".env"

settings = Settings()
