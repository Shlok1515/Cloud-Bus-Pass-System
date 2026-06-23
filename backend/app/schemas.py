from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class BusCreate(BaseModel):
    bus_name: str
    source: str
    destination: str
    total_seats: int
    fare: int

class BookingCreate(BaseModel):
    user_id: int
    bus_id: int
    seats_booked: int
