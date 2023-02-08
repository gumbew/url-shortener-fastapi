from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings
from url_shortener.models import ShortUrl


async def init() -> None:
    client = AsyncIOMotorClient(settings.DATABASE_URI, uuidRepresentation="standard")

    await init_beanie(
        database=getattr(client, settings.MONGO_DATABASE_NAME),
        document_models=[ShortUrl]
    )
