from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class SHotels(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels")
def get_hotels(
    locations: str,
    date_from: date,
    date_to: date,
    has_spa: bool|None,
    stars: Optional[int] = Query(None, ge=1, le=5),
) -> list[SHotels]:
    hotels = [
        {
            "address": "ул. Гагарина, 1, Алтай",
            "name": "Super Hotel",
            "stars": 5,
        }
    ]
    
    return hotels

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
    
@app.post("/booking")
def add_booking(booking: SBooking):
    pass