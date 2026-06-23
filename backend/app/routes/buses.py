from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Bus
from ..schemas import BusCreate

router = APIRouter(
    prefix="/buses",
    tags=["Buses"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add")
def add_bus(bus: BusCreate, db: Session = Depends(get_db)):

    new_bus = Bus(
        bus_name=bus.bus_name,
        source=bus.source,
        destination=bus.destination,
        total_seats=bus.total_seats,
        fare=bus.fare
    )

    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)

    return {
        "message": "Bus added successfully",
        "bus_id": new_bus.bus_id
    }


@router.get("/")
def get_all_buses(db: Session = Depends(get_db)):
    return db.query(Bus).all()

@router.get("/search")
def search_bus(
    source: str,
    destination: str,
    db: Session = Depends(get_db)
):
    buses = db.query(Bus).filter(
        Bus.source == source,
        Bus.destination == destination
    ).all()

    return buses