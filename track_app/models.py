from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Rail(Base):
    __tablename__ = 'rails'
    id = Column(Integer, primary_key=True)
    profile = Column(String, nullable=False)  # e.g., BS-95R
    length = Column(Float, nullable=False)  # Rail length in mm
    scale = Column(String, nullable=False)  # Scale, e.g., OO-BF

class Chair(Base):
    __tablename__ = 'chairs'
    id = Column(Integer, primary_key=True)
    slot_depth = Column(Float, nullable=False)
    slot_width = Column(Float, nullable=False)
    tolerance = Column(Float, nullable=False)
    rail_id = Column(Integer, ForeignKey('rails.id'))
    rail = relationship("Rail", back_populates="chairs")

class StraightTrack(Base):
    __tablename__ = 'straight_tracks'
    id = Column(Integer, primary_key=True)
    length = Column(Float, nullable=False)
    chair_spacing = Column(Float, nullable=False)
    sleeper_spacing = Column(Float, nullable=False)
    rail_id = Column(Integer, ForeignKey('rails.id'))
    rail = relationship("Rail")

