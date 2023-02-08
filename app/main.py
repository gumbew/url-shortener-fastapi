from fastapi import FastAPI

from db import init_db

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db.init()


@app.get("/")
async def root():
    return {"message": "Hello World"}
