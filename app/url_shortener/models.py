from datetime import datetime, timedelta
from typing import Optional

from beanie import Document, Indexed
from pydantic import Field

from url_shortener.services import generate_short_url


class ShortUrl(Document):
    short_url: Indexed(str, unique=True)
    origin: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[Indexed(datetime, expireAfterSeconds=0)] = None

    @classmethod
    async def shorten(
            cls,
            *,
            url: str,
            expiration_days: Optional[float] = None,
    ) -> "ShortUrl":
        return await cls(
            short_url=generate_short_url(url),
            origin=url,
            expires_at=(
                datetime.utcnow() + timedelta(days=expiration_days)
                if expiration_days
                else None
            ),
        ).insert()

    @classmethod
    async def get_by_short_url(cls, *, short_url: str) -> Optional["ShortUrl"]:
        return await cls.find_one(cls.short_url == short_url)

    class Settings:
        name = "urls"
