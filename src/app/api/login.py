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
@router.get("/login/{guest_number}", tags=["Login endpoint"])
async def get_family(guest_number: str, db: Session = Depends(get_db)):
    
    db_family = crud.get_guest(db, phone_number=guest_number)
    assistants_number = crud.get_assistants(db, phone_number=guest_number)
    
    if db_family is None:
        raise HTTPException(status_code=404, detail="User not found")

    elif assistants_number is None:
         raise HTTPException(status_code=404, detail="Number of assistants not found")

    return {'family_name':f'{db_family.family.family_name}',
            'attendance_confirmation': f'{db_family.attendance_confirmation}',
            'Number_of_assistants': f'{assistants_number}'}