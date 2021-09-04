from fastapi import FastAPI

app = FastAPI()



@app.get("/ping")
def pong():
    return {"ping": "pong!"}


@app.get('/', tags=["API Landing"])
def welcome():
    return {"title": "Backend API for the wedding project"}
