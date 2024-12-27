from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.database import get_session
from app.models import Timber

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

@router.put("/{timber_id}", response_model=Timber)
def update_timber(timber_id: int, timber: Timber, session: Session = Depends(get_session)):
    existing_timber = session.get(Timber, timber_id)
    if not existing_timber:
        raise HTTPException(status_code=404, detail="Timber not found")
    for key, value in timber.dict(exclude_unset=True).items():
        setattr(existing_timber, key, value)
    session.commit()
    session.refresh(existing_timber)
    return existing_timber

@router.delete("/{timber_id}", response_model=dict)
def delete_timber(timber_id: int, session: Session = Depends(get_session)):
    timber = session.get(Timber, timber_id)
    if not timber:
        raise HTTPException(status_code=404, detail="Timber not found")
    session.delete(timber)
    session.commit()
    return {"message": "Timber deleted successfully"}
