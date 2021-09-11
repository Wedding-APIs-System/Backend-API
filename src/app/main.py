from fastapi import FastAPI
from app.api import landing, login
from sql_app.database import orm_connection


app = FastAPI()

app.include_router(landing.router)
app.include_router(login.router)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}



