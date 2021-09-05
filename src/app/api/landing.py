from fastapi import APIRouter

router = APIRouter()

@router.get('/', tags=["API Landing"])
async def welcome():
    return {"title": "Backend API for the wedding project"}