from pydantic import BaseModel
from typing import Optional

class Family(BaseModel):
    family_id: int
    family_name: str

    class Config:
        orm_mode = True

class GuestAssistance(BaseModel):
    attendance_confirmation: bool
    allergies: Optional[str]
    additional_comments: Optional[str]

class GuestBase(BaseModel):
    phone_number: str

class Guest(GuestBase):
    guest_id: int
    family_id: int
    name: str
    attendance_confirmation: Optional[bool]
    allergies: Optional[str]
    additional_comments: Optional[str]

    class Config:
        orm_mode = True

class GuestFamily(BaseModel):
    family_name: str

