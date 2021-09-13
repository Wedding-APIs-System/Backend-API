from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import landing, login, attendance_confirmation
from sql_app.database import orm_connection


app = FastAPI(title="Sergio's wedding backend API",
    description="REST API which serves login, attendance confirmation and other features",
    version="1.0",)

origins = [
    "*"
    # "http://190.96.140.12:5500",
    # "68.251.63.208"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(landing.router)
app.include_router(login.router)
app.include_router(attendance_confirmation.router)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}



