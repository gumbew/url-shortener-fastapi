import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, MongoDsn, validator


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    MONGO_HOST: str
    MONGO_ROOT_USER: str
    MONGO_ROOT_PASSWORD: str
    MONGO_DATABASE_NAME: str

    DATABASE_URI: Optional[MongoDsn] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return MongoDsn.build(
            scheme="mongodb",
            user=values.get("MONGO_ROOT_USER"),
            password=values.get("MONGO_ROOT_PASSWORD"),
            host=values.get("MONGO_HOST"),
            path=f"/{values.get('MONGO_DATABASE_NAME') or ''}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
