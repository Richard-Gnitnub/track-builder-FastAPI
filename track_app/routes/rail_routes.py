from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from track_app.database import get_session
from track_app.models import Rail

router = APIRouter()

@router.post("/", response_model=Rail)
def create_rail(rail: Rail, session: Session = Depends(get_session)):
    session.add(rail)
    session.commit()
    session.refresh(rail)
    return rail

@router.get("/", response_model=list[Rail])
def read_rails(session: Session = Depends(get_session)):
    statement = select(Rail)
    results = session.exec(statement).all()
    return results

@router.put("/{rail_id}", response_model=Rail)
def update_rail(rail_id: int, rail: Rail, session: Session = Depends(get_session)):
    existing_rail = session.get(Rail, rail_id)
    if not existing_rail:
        raise HTTPException(status_code=404, detail="Rail not found")
    for key, value in rail.dict(exclude_unset=True).items():
        setattr(existing_rail, key, value)
    session.commit()
    session.refresh(existing_rail)
    return existing_rail

@router.delete("/{rail_id}", response_model=dict)
def delete_rail(rail_id: int, session: Session = Depends(get_session)):
    rail = session.get(Rail, rail_id)
    if not rail:
        raise HTTPException(status_code=404, detail="Rail not found")
    session.delete(rail)
    session.commit()
    return {"message": "Rail deleted successfully"}
