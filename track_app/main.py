from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from fastapi_admin.models import ModelAdmin
from fastapi_admin.providers.login import UsernamePasswordProvider
from track_app.routes.rail_routes import router as rail_router
from track_app.routes.chair_routes import router as chair_router
from track_app.routes.track_routes import router as track_router
from track_app.routes.timber_routes import router as timber_router
from track_app.routes.stl_routes import router as stl_router
from track_app.models import AdminUser, Rail, Chair, StraightTrack, Timber
from track_app.database import engine  # Your database connection

app = FastAPI()

# Initialize fastapi-admin
@app.on_event("startup")
async def startup():
    await admin_app.init(
        engine=engine,
        admin_secret="super_secure_secret",  # Replace with a secure key
        providers=[
            UsernamePasswordProvider(
                username="admin",
                password="admin123",  # Replace with secure credentials
            )
        ],
    )
    # Register admin models
    admin_app.register(ModelAdmin(model=AdminUser))
    admin_app.register(ModelAdmin(model=Rail))
    admin_app.register(ModelAdmin(model=Chair))
    admin_app.register(ModelAdmin(model=StraightTrack))
    admin_app.register(ModelAdmin(model=Timber))

# Include existing routes
app.include_router(rail_router, prefix="/api/rails", tags=["Rails"])
app.include_router(chair_router, prefix="/api/chairs", tags=["Chairs"])
app.include_router(track_router, prefix="/api/straight-tracks", tags=["Straight Tracks"])
app.include_router(timber_router, prefix="/api/timbers", tags=["Timbers"])
app.include_router(stl_router, prefix="/api/stl", tags=["STL Files"])

# Mount the admin interface
app.mount("/admin", admin_app)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Lightweight Track Builder API"}
