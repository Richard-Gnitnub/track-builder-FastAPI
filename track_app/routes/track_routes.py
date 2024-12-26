from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.database import get_session
from app.models import StraightTrack

router = APIRouter()

@router.post("/", response_model=StraightTrack)
def create_straight_track(straight_track: StraightTrack, session: Session = Depends(get_session)):
    session.add(straight_track)
    session.commit()
    session.refresh(straight_track)
    return straight_track

@router.get("/", response_model=list[StraightTrack])
def read_straight_tracks(session: Session = Depends(get_session)):
    statement = select(StraightTrack)
    results = session.exec(statement).all()
    return results
