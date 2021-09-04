from fastapi import FastAPI
from app.api import landing

app = FastAPI()

app.include_router(landing.router)

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}



