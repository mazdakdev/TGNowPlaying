from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SPOTIFY_CLIENT_ID: str
    SPOTIFY_CLIENT_SECRET: str
    SPOTIFY_REDIRECT_URI: str
    API_ID: int
    API_HASH: str
    CHANNEL_ID: int

    class Config:
        env_file = ".env"

settings = Settings()
