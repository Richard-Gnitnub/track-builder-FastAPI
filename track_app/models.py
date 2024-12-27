from sqlmodel import SQLModel, Field, Relationship, Session, select
from typing import List, Optional
from track_app.enums import ChairType
# track_app/models.py

class Timber(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    length: float
    width: float
    depth: float
    flange_width: Optional[float] = None
    flange_depth: Optional[float] = None
    position: float
    track_id: Optional[int] = Field(default=None, foreign_key="track.id")

    # Add this relationship so "timbers" <-> "track" match
    track: Optional["Track"] = Relationship(back_populates="timbers")


class Chair(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    groove_width: float
    groove_depth: float
    fit_adjustment: Optional[float] = 0.0
    rib_spacing: Optional[float] = None
    jaw_height: Optional[float] = None
    placement_offset: float
    timber_id: Optional[int] = Field(default=None, foreign_key="timber.id")
    track_id: Optional[int] = Field(default=None, foreign_key="track.id")
    type: ChairType = Field(default=ChairType.S1)

    # Add this relationship so "chairs" <-> "track" match
    track: Optional["Track"] = Relationship(back_populates="chairs")


class Track(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total_length: float
    timber_spacing: float
    chair_alignment: str

    timbers: List["Timber"] = Relationship(back_populates="track")
    chairs: List["Chair"] = Relationship(back_populates="track")
