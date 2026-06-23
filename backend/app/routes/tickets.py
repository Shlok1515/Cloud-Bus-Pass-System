from fastapi import APIRouter
import qrcode
import json
import os

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@router.get("/generate/{booking_id}")
def generate_ticket(booking_id: int):

    ticket_data = {
        "booking_id": booking_id
    }

    os.makedirs("tickets", exist_ok=True)

    filename = f"tickets/ticket_{booking_id}.png"

    qr = qrcode.make(
        json.dumps(ticket_data)
    )

    qr.save(filename)

    return {
        "message": "Ticket generated successfully",
        "file": filename
    }