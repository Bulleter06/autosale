import asyncio
from models.car import Car
from modules.database import Base, sessionmanager


async def init_models():
    async with sessionmanager.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_models())
