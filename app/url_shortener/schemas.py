from typing import Optional

from pydantic import AnyUrl, BaseModel, Field


class ShortUrlCreate(BaseModel):
    url: AnyUrl
    expiration_days: Optional[int] = Field(90, gt=0, le=365)
