from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
# from .database import SessionLocal, engine
from .database import orm_connection

# SessionLocal, engine = orm_connection()
# models.Base.metadata.create_all(bind=engine)

def get_assistants(db: Session, phone_number: str):
    guest_object = db.query(models.Guest).filter(models.Guest.phone_number == phone_number).first()
    if guest_object is not None:
        family_id = guest_object.family_id
        asstants_number = db.query(models.Guest).filter(models.Guest.family_id == family_id).count()
        return asstants_number

    else:
        return None

def get_guest(db: Session, phone_number: str):
    guest_object = db.query(models.Guest).filter(models.Guest.phone_number == phone_number).first()
    if guest_object is not None:
        return guest_object
    else:
        return None

def get_family_members(db: Session, phone_number: str):
    guest_object = db.query(models.Guest).filter(models.Guest.phone_number == phone_number).first()
    
    if guest_object is not None:
        family_id = guest_object.family_id
        members_list = db.query(models.Guest).filter(models.Guest.family_id == family_id).all()
        return members_list
    else:
        return None

def confirm_assistance(db: Session, confirmation: schemas.GuestAssistance, phone_number: str()):
    # guest_info = models.Guest(**confirmation, phone_number=phone_number)
    guest_info = get_guest(db, phone_number)
    family_members = get_family_members(db, phone_number)
    

    if family_members and guest_info is not None:
        # update the allergies  and the additional comments for the user doing the confirmation
        guest_info.allergies = confirmation.allergies
        guest_info.additional_comments = confirmation.additional_comments
        db.commit()
        db.refresh(guest_info)

        # Go through the list of members of the same family
        for member in family_members:
            member.attendance_confirmation = confirmation.attendance_confirmation
            db.commit()
            # refreshing means to expire and then immediately get the latest data for
            # the object from the database.
            db.refresh(member)      
            
        updated_members = get_family_members(db, phone_number)

        return updated_members
    # Save and refresh the changes on the db
    

    # if guest_info is not None:
    #     #Update the attendance confirmation
    #     guest_info.attendance_confirmation = confirmation.attendance_confirmation

    #     #Save and refresh the changes on the db
    #     db.commit()
    #     db.refresh(guest_info)

    #     return guest_info
    
    else:
        raise HTTPException(status_code=404, detail="Validation Error, the number doesn't exist")


# *************THe following section was to test if the crud was working *************

# if __name__=='__main__':
    
#     SessionLocal, engine = orm_connection()
#     models.Base.metadata.create_all(bind=engine)

#     db = SessionLocal()
#     db_guest = get_guest(db, '3105585460')
#     print(db_guest.family.family_name)