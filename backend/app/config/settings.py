from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "ESSA - Electronics Engineering Students Association"
    SECRET_KEY: str = "essa_secret_jwt_key_terna_engineering_students_association"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    DATABASE_URL: str = "sqlite:///./essa.db"
    ADMIN_USERNAME: str = "admin"
    ADMIN_PASSWORD: str = "adminpassword123"
    ADMIN_EMAIL: str = "admin@ternaengg.ac.in"
    UPLOAD_DIR: str = "uploads"

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
