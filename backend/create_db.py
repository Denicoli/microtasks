from app.database import engine
from app.models import Base
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    import asyncio
    asyncio.run(create_db())
