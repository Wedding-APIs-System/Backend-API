from sqlalchemy.orm import Session
from . import models, schemas
# from .database import SessionLocal, engine
from .database import orm_connection

# SessionLocal, engine = orm_connection()
# models.Base.metadata.create_all(bind=engine)


def get_guest(db: Session, phone_number: str):
    guest_object = db.query(models.Guest).filter(models.Guest.phone_number == phone_number).first()
    if guest_object is not None:
        return guest_object.family.family_name

    else:
        return None

# *************THe following section was to test if the crud was working *************

# if __name__=='__main__':
    
#     SessionLocal, engine = orm_connection()
#     models.Base.metadata.create_all(bind=engine)

#     db = SessionLocal()
#     db_guest = get_guest(db, '3105585460')
#     print(db_guest.family.family_name)