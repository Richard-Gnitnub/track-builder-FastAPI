from fastapi import FastAPI
from app.routes.rail_routes import router as rail_router
from app.routes.chair_routes import router as chair_router
from app.routes.track_routes import router as track_router
from app.routes.timber_routes import router as timber_router
from app.routes.stl_routes import router as stl_router

app = FastAPI()

# Include routes
app.include_router(rail_router, prefix="/api/rails", tags=["Rails"])
app.include_router(chair_router, prefix="/api/chairs", tags=["Chairs"])
app.include_router(track_router, prefix="/api/straight-tracks", tags=["Straight Tracks"])
app.include_router(timber_router, prefix="/api/timbers", tags=["Timbers"])
app.include_router(stl_router, prefix="/api/stl", tags=["STL Files"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Lightweight Track Builder API"}
