from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from track_app.database import get_session
from track_app.models import Chair

router = APIRouter()

@router.post("/", response_model=Chair)
def create_chair(chair: Chair, session: Session = Depends(get_session)):
    session.add(chair)
    session.commit()
    session.refresh(chair)
    return chair

@router.get("/", response_model=list[Chair])
def read_chairs(session: Session = Depends(get_session)):
    statement = select(Chair)
    results = session.exec(statement).all()
    return results
