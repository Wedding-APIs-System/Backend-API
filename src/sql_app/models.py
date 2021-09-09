from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

class Family(Base):
    __tablename__ = "families"

    family_id = Column(Integer, primary_key=True, index=True)
    family_name = Column(String, unique=True, nullable=False)
    guests = relationship("Guest", back_populates="family")

class Guest(Base):
    __tablename__ = "guests"

    guest_id = Column(Integer, primary_key=True, index=True)
    family_id = Column(Integer, ForeignKey("families.family_id"), nullable=False)
    name = Column(String, nullable=False)
    phone_number = Column(String)
    attendance_confirmation = Column(Boolean, default=False)
    allergies = Column(String)
    additional_comments =  Column(String)
    family = relationship("Family", back_populates="guests")