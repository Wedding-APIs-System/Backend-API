from sqlalchemy.orm import Session
from . import models, schemas
# from .database import SessionLocal, engine
from .database import orm_connection

# SessionLocal, engine = orm_connection()
# models.Base.metadata.create_all(bind=engine)


def get_guest(db: Session, phone_number: str):
    guest_object = db.query(models.Guest).filter(models.Guest.phone_number == phone_number).first()
    if guest_object is not None:
        return guest_object
    else:
        return None

def confirm_assistance(db: Session, confirmation: schemas.GuestAssistance, phone_number: str()):
    # guest_info = models.Guest(**confirmation, phone_number=phone_number)
    guest_info = get_guest(db, phone_number)
    #Update the attendance confirmation
    guest_info.attendance_confirmation = confirmation.attendance_confirmation

    #Save and refresh the changes on the db
    db.commit()
    db.refresh(guest_info)

    return guest_info


# *************THe following section was to test if the crud was working *************

# if __name__=='__main__':
    
#     SessionLocal, engine = orm_connection()
#     models.Base.metadata.create_all(bind=engine)

#     db = SessionLocal()
#     db_guest = get_guest(db, '3105585460')
#     print(db_guest.family.family_name)