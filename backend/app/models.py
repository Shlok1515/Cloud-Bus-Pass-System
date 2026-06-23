from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(255))


class Bus(Base):
    __tablename__ = "buses"

    bus_id = Column(Integer, primary_key=True, index=True)
    bus_name = Column(String(100))
    source = Column(String(100))
    destination = Column(String(100))
    total_seats = Column(Integer)
    fare = Column(Integer)


class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    bus_id = Column(Integer, ForeignKey("buses.bus_id"))
    seats_booked = Column(Integer)

    # Booking timestamp
    booking_time = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
    bus = relationship("Bus")