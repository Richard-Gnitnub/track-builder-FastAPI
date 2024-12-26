from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Rail(SQLModel, table=True):
    __tablename__ = "rails"
    id: Optional[int] = Field(default=None, primary_key=True)
    profile: str = Field(..., description="Rail profile (e.g., BS-95R)")
    length: float = Field(..., description="Length of the rail in mm")
    scale: str = Field(..., description="Scale of the rail, e.g., OO-BF")

class Chair(SQLModel, table=True):
    __tablename__ = "chairs"
    id: Optional[int] = Field(default=None, primary_key=True)
    slot_depth: float = Field(..., description="Depth of the chair slot for the rail foot")
    slot_width: float = Field(..., description="Width of the chair slot for the rail foot")
    tolerance: float = Field(..., description="Assembly tolerance for the chair slot")
    rail_id: Optional[int] = Field(default=None, foreign_key="rails.id")

class StraightTrack(SQLModel, table=True):
    __tablename__ = "straight_tracks"
    id: Optional[int] = Field(default=None, primary_key=True)
    length: float = Field(..., description="Total length of the track in mm")
    chair_spacing: float = Field(..., description="Spacing between chairs on the track")
    sleeper_spacing: float = Field(..., description="Spacing between sleepers on the track")
    rail_id: Optional[int] = Field(default=None, foreign_key="rails.id")

class Timber(SQLModel, table=True):
    __tablename__ = "timbers"
    id: Optional[int] = Field(default=None, primary_key=True)
    position: float = Field(..., description="Position of the timber along the track")
    width: float = Field(..., description="Width of the timber in mm")
    thickness: float = Field(..., description="Thickness of the timber in mm")
    material: str = Field(..., description="Material type of the timber")
