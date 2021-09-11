from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sql_app.database import orm_connection
from sql_app import schemas, models, crud

SessionLocal, engine = orm_connection()
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

# @router.get("/login/{guest_number}", response_model=schemas.GuestFamily)
@router.get("/login/{guest_number}")
async def get_family(guest_number: str, db: Session = Depends(get_db)):
    db_family = crud.get_guest(db, phone_number=guest_number)
    if db_family is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_family