from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Timber(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    length: float = Field(..., description="Length of the timber in mm")
    width: float = Field(..., description="Width of the timber in mm")
    depth: float = Field(..., description="Depth of the timber in mm")
    flange_width: Optional[float] = Field(default=None, description="Width of the flange in mm")
    flange_depth: Optional[float] = Field(default=None, description="Depth of the flange in mm")
    position: float = Field(..., description="Position of the timber along the track")
    track_id: Optional[int] = Field(default=None, foreign_key="track.id")

class Chair(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    groove_width: float = Field(..., description="Width of the groove for the rail foot in mm")
    groove_depth: float = Field(..., description="Depth of the groove for the rail foot in mm")
    fit_adjustment: Optional[float] = Field(default=0.0, description="Adjustment for printing tolerances in mm")
    rib_spacing: Optional[float] = Field(default=None, description="Spacing between ribs on the chair")
    jaw_height: Optional[float] = Field(default=None, description="Height of the chair jaw in mm")
    placement_offset: float = Field(..., description="Offset of the chair along the timber in mm")
    timber_id: Optional[int] = Field(default=None, foreign_key="timber.id")

class Track(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total_length: float = Field(..., description="Total length of the track in mm")
    timber_spacing: float = Field(..., description="Spacing between timbers in mm")
    chair_alignment: str = Field(..., description="Alignment pattern for chairs (e.g., 'opposite', 'staggered')")
    timbers: List[Timber] = Relationship(back_populates="track")
    chairs: List[Chair] = Relationship(back_populates="track")
