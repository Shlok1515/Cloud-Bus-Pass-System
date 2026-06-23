from fastapi import FastAPI
from .database import engine
from . import models
from .routes import users, buses
from .routes import users, buses, bookings
from .routes import users, buses, bookings, tickets
from .routes import analytics
# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Cloud Bus Pass System"
)

# Register routers
app.include_router(users.router)
app.include_router(buses.router)
app.include_router(bookings.router)
app.include_router(tickets.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {
        "message": "Cloud Bus Pass System Running"
    }