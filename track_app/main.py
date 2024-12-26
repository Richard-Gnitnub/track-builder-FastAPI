from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from track_app.routes.rail_routes import router as rail_router
from track_app.routes.chair_routes import router as chair_router
from track_app.routes.track_routes import router as track_router
from track_app.routes.timber_routes import router as timber_router
from track_app.routes.stl_routes import router as stl_router

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="track_app/templates")

# Admin routes for all models
app.include_router(rail_router, prefix="/admin/rails", tags=["Admin: Rails"])
app.include_router(chair_router, prefix="/admin/chairs", tags=["Admin: Chairs"])
app.include_router(track_router, prefix="/admin/tracks", tags=["Admin: Tracks"])
app.include_router(timber_router, prefix="/admin/timbers", tags=["Admin: Timbers"])
app.include_router(stl_router, prefix="/admin/stl", tags=["Admin: STL Operations"])

# Admin dashboard route
@app.get("/admin", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request})

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Lightweight Track Builder API"}

#health check
@app.get("/health", response_class=HTMLResponse)
def health_check():
    return {"status": "healthy"}
