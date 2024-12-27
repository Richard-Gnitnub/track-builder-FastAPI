from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from track_app.database import get_session
from track_app.models import Track

router = APIRouter()

@router.post("/", response_model=Track)
def create_track(track: Track, session: Session = Depends(get_session)):
    session.add(track)
    session.commit()
    session.refresh(track)
    return track

@router.get("/", response_model=list[Track])
def read_tracks(session: Session = Depends(get_session)):
    statement = select(Track)
    results = session.exec(statement).all()
    return results

@router.put("/{track_id}", response_model=Track)
def update_track(track_id: int, track: Track, session: Session = Depends(get_session)):
    existing_track = session.get(Track, track_id)
    if not existing_track:
        raise HTTPException(status_code=404, detail="Track not found")
    for key, value in track.dict(exclude_unset=True).items():
        setattr(existing_track, key, value)
    session.commit()
    session.refresh(existing_track)
    return existing_track

@router.delete("/{track_id}", response_model=dict)
def delete_track(track_id: int, session: Session = Depends(get_session)):
    track = session.get(Track, track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    session.delete(track)
    session.commit()
    return {"message": "Track deleted successfully"}
