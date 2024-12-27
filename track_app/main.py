from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Import routers for CRUD operations
from track_app.routes.chair_routes import router as chair_router
from track_app.routes.track_routes import router as track_router
from track_app.routes.timber_routes import router as timber_router
from track_app.routes.stl_routes import router as stl_router

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="track_app/templates")

# Admin routes for CRUD operations
app.include_router(chair_router, prefix="/admin/chairs", tags=["Admin: Chairs"])
app.include_router(track_router, prefix="/admin/tracks", tags=["Admin: Tracks"])
app.include_router(timber_router, prefix="/admin/timbers", tags=["Admin: Timbers"])
app.include_router(stl_router, prefix="/admin/stl", tags=["Admin: STL Operations"])

# Landing page route
@app.get("/", response_class=HTMLResponse)
def landing_page(request: Request):
    return templates.TemplateResponse("landing_page.html", {"request": request})

# Dashboard route
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# About page route
@app.get("/about", response_class=HTMLResponse)
def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Contact page route
@app.get("/contact", response_class=HTMLResponse)
def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# Root endpoint for API message (optional)
@app.get("/api")
def read_root():
    return {"message": "Welcome to the Lightweight Track Builder API"}
