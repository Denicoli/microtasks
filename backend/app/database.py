from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import DevelopmentConfig
from dotenv import load_dotenv

load_dotenv()

# Load database URL from environment variables
DATABASE_URL = DevelopmentConfig.DATABASE_URL

# Create asynchronous engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session maker for creating sessions in the database
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class for SQLAlchemy models
Base = declarative_base()

# Dependency to get the session in API routes
async def get_db():
    async with SessionLocal() as session:
        yield session
