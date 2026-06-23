from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Booking, Bus
from ..schemas import BookingCreate
from ..models import Booking, Bus, User

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/book")
def book_ticket(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    bus = db.query(Bus).filter(
        Bus.bus_id == booking.bus_id
    ).first()

    if not bus:
        return {"message": "Bus not found"}

    total_bookings = db.query(Booking).filter(
        Booking.bus_id == booking.bus_id
    ).all()

    booked_seats = sum(
        b.seats_booked for b in total_bookings
    )

    available_seats = (
        bus.total_seats - booked_seats
    )

    if booking.seats_booked > available_seats:
        return {
            "message": "Not enough seats available",
            "available_seats": available_seats
        }

    new_booking = Booking(
        user_id=booking.user_id,
        bus_id=booking.bus_id,
        seats_booked=booking.seats_booked
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return {
        "message": "Ticket booked successfully",
        "booking_id": new_booking.booking_id,
        "available_seats": available_seats - booking.seats_booked
    }


@router.get("/availability/{bus_id}")
def check_seat_availability(
    bus_id: int,
    db: Session = Depends(get_db)
):

    bus = db.query(Bus).filter(
        Bus.bus_id == bus_id
    ).first()

    if not bus:
        return {"message": "Bus not found"}

    bookings = db.query(Booking).filter(
        Booking.bus_id == bus_id
    ).all()

    booked_seats = sum(
        booking.seats_booked for booking in bookings
    )

    available_seats = (
        bus.total_seats - booked_seats
    )

    return {
        "bus_id": bus.bus_id,
        "bus_name": bus.bus_name,
        "total_seats": bus.total_seats,
        "booked_seats": booked_seats,
        "available_seats": available_seats,
        "occupancy_percentage": round(
            (booked_seats / bus.total_seats) * 100,
            2
        )
    }

@router.get("/user/{user_id}")
def get_user_bookings(
    user_id: int,
    db: Session = Depends(get_db)
):

    bookings = db.query(Booking).filter(
        Booking.user_id == user_id
    ).all()

    result = []

    for booking in bookings:

        bus = db.query(Bus).filter(
            Bus.bus_id == booking.bus_id
        ).first()

        result.append({
            "booking_id": booking.booking_id,
            "bus_name": bus.bus_name,
            "source": bus.source,
            "destination": bus.destination,
            "fare": bus.fare,
            "seats_booked": booking.seats_booked
        })

    return result