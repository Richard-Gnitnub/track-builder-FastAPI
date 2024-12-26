from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from track_app.database import get_session
from track_app.models import Timber

router = APIRouter()

@router.post("/", response_model=Timber)
def create_timber(timber: Timber, session: Session = Depends(get_session)):
    session.add(timber)
    session.commit()
    session.refresh(timber)
    return timber

@router.get("/", response_model=list[Timber])
def read_timbers(session: Session = Depends(get_session)):
    statement = select(Timber)
    results = session.exec(statement).all()
    return results
