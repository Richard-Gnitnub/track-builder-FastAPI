from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.database import get_session
from app.models import Rail, Chair, StraightTrack

router = APIRouter()

# Rails Endpoints
@router.post("/rails/", response_model=Rail)
def create_rail(rail: Rail, session: Session = Depends(get_session)):
    session.add(rail)
    session.commit()
    session.refresh(rail)
    return rail

@router.get("/rails/", response_model=list[Rail])
def read_rails(session: Session = Depends(get_session)):
    statement = select(Rail)
    results = session.exec(statement).all()
    return results

# Chairs Endpoints
@router.post("/chairs/", response_model=Chair)
def create_chair(chair: Chair, session: Session = Depends(get_session)):
    session.add(chair)
    session.commit()
    session.refresh(chair)
    return chair

@router.get("/chairs/", response_model=list[Chair])
def read_chairs(session: Session = Depends(get_session)):
    statement = select(Chair)
    results = session.exec(statement).all()
    return results

# Straight Tracks Endpoints
@router.post("/straight-tracks/", response_model=StraightTrack)
def create_straight_track(straight_track: StraightTrack, session: Session = Depends(get_session)):
    session.add(straight_track)
    session.commit()
    session.refresh(straight_track)
    return straight_track

@router.get("/straight-tracks/", response_model=list[StraightTrack])
def read_straight_tracks(session: Session = Depends(get_session)):
    statement = select(StraightTrack)
    results = session.exec(statement).all()
    return results
