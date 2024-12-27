from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from track_app.database import get_session
from track_app.models import Track
from track_app.stl_generator import generate_stl_file  # Assuming a separate module for STL logic

router = APIRouter()

@router.post("/generate/", response_model=str)
def generate_straight_track_stl(track_id: int, session: Session = Depends(get_session)):
    # Fetch the straight track by ID
    track = session.get(StraightTrack, track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")

    # Generate the STL file
    stl_path = generate_stl_file(track)
    if not stl_path:
        raise HTTPException(status_code=500, detail="Failed to generate STL file")

    return stl_path

@router.get("/download/{file_name}")
def download_stl(file_name: str):
    # Path to STL file directory
    stl_dir = "stl_files/"
    stl_file_path = f"{stl_dir}{file_name}"

    try:
        return FileResponse(stl_file_path, media_type="application/octet-stream", filename=file_name)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
