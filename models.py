# models.py
from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class BodyPerformance(Base):
    __tablename__ = "body_performance"
    
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)
    weight_kg = Column(Float, nullable=False)
    body_fat = Column(Float, nullable=False)
    diastolic = Column(Integer, nullable=False)
    sit_and_bend_forward_cm = Column(Float, nullable=False)
    sit_ups_counts = Column(Integer, nullable=False)
    broad_jump_cm = Column(Float, nullable=False)