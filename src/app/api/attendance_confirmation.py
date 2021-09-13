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


@router.put("/confirmation/{guest_number}", tags=["Confirmation endpoint"])
async def confirm_assistance(guest_number: str, confirmation: schemas.GuestAssistance, db: Session = Depends(get_db)):
    guest_info = crud.confirm_assistance(db, confirmation=confirmation, phone_number=guest_number)
    if guest_info is None:
        raise HTTPException(status_code=404, detail="Validation Error")
    return guest_info