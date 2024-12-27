from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.routes.timber_routes import router as timber_router
from app.routes.chair_routes import router as chair_router
from app.routes.track_routes import router as track_router

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Admin routes for all models
app.include_router(timber_router, prefix="/admin/timbers", tags=["Admin: Timbers"])
app.include_router(chair_router, prefix="/admin/chairs", tags=["Admin: Chairs"])
app.include_router(track_router, prefix="/admin/tracks", tags=["Admin: Tracks"])

# Admin dashboard route
@app.get("/admin", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request})

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Lightweight Track Builder API"}
