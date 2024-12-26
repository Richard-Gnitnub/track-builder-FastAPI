from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Track(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # Track identifier
    length: float  # Length of the track in mm
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Timber(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    track_id: int = Field(foreign_key="track.id")  # Foreign key to Track
    position: float  # Position along the track
    width: float  # Timber width
    thickness: float  # Timber thickness
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Chair(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timber_id: int = Field(foreign_key="timber.id")  # Foreign key to Timber
    type: str  # Chair type
    position: float  # Position relative to the timber
    created_at: datetime = Field(default_factory=datetime.utcnow)

class STLFile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    track_id: int = Field(foreign_key="track.id")  # Foreign key to Track
    filename: str  # STL file name
    is_valid: bool = Field(default=True)  # Indicates if the STL is valid
    created_at: datetime = Field(default_factory=datetime.utcnow)
