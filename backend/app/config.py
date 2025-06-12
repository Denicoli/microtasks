import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base config class."""
    # General configuration
    APP_NAME = "MicroTasks API"
    DEBUG = True

class DevelopmentConfig(Config):
    """Development specific configurations."""
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DATABASE_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}"

