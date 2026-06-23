from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..database import SessionLocal
from ..models import User, Bus, Booking

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/summary")
def analytics_summary(
    db: Session = Depends(get_db)
):

    total_users = db.query(User).count()

    total_buses = db.query(Bus).count()

    total_bookings = db.query(Booking).count()

    total_revenue = (
        db.query(
            func.sum(
                Booking.seats_booked * Bus.fare
            )
        )
        .join(
            Bus,
            Booking.bus_id == Bus.bus_id
        )
        .scalar()
    )

    if total_revenue is None:
        total_revenue = 0

    return {
        "total_users": total_users,
        "total_buses": total_buses,
        "total_bookings": total_bookings,
        "total_revenue": total_revenue
    }