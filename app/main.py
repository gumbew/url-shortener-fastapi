from fastapi import FastAPI

from db import init_db
from url_shortener.routers import url_shortener_router

app = FastAPI()

app.include_router(url_shortener_router)


@app.on_event("startup")
async def on_startup():
    await init_db.init()


@app.get("/")
async def root():
    return {"message": "Hello World"}
