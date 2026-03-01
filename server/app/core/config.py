from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Converter API"
    API_V1_PREFIX: str = "/api/v1"
    STORAGE_TYPE: str = "local"
    UPLOAD_DIR: str = "uploads"

    class Config:
        env_file = ".env"

settings = Settings()