from pydantic import BaseModel
from typing import Optional

class Family(BaseModel):
    family_id: int
    family_name: str

    class Config:
        orm_mode = True

class Guest(BaseModel):
    guest_id: int
    family_id: int
    name: str
    phone_number: str
    attendance_confirmation: Optional[str]
    allergies: Optional[str]
    additional_comments: Optional[str]

    class Config:
        orm_mode = True

