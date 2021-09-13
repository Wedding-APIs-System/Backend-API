from fastapi import FastAPI
from app.api import landing, login, attendance_confirmation
from sql_app.database import orm_connection


app = FastAPI()

app.include_router(landing.router)
app.include_router(login.router)
app.include_router(attendance_confirmation.router)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}



