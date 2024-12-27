from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.database import get_session
from app.models import Chair

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

@router.put("/{chair_id}", response_model=Chair)
def update_chair(chair_id: int, chair: Chair, session: Session = Depends(get_session)):
    existing_chair = session.get(Chair, chair_id)
    if not existing_chair:
        raise HTTPException(status_code=404, detail="Chair not found")
    for key, value in chair.dict(exclude_unset=True).items():
        setattr(existing_chair, key, value)
    session.commit()
    session.refresh(existing_chair)
    return existing_chair

@router.delete("/{chair_id}", response_model=dict)
def delete_chair(chair_id: int, session: Session = Depends(get_session)):
    chair = session.get(Chair, chair_id)
    if not chair:
        raise HTTPException(status_code=404, detail="Chair not found")
    session.delete(chair)
    session.commit()
    return {"message": "Chair deleted successfully"}
