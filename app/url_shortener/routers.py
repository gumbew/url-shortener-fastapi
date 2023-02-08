from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse

from url_shortener.models import ShortUrl
from url_shortener.schemas import ShortUrlCreate

url_shortener_router = APIRouter(tags=["URL Shortener"])


@url_shortener_router.post("/shorten", response_model=ShortUrl)
async def shorten_url(payload: ShortUrlCreate) -> ShortUrl:
    short_url = await ShortUrl.shorten(
        url=payload.url,
        expiration_days=payload.expiration_days,
    )
    return short_url


@url_shortener_router.get("/{short_url}", response_class=RedirectResponse)
async def redirect_by_short_url(short_url: str) -> str:
    if short_url := await ShortUrl.get_by_short_url(short_url=short_url):
        return short_url.origin
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
