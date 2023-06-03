import strawberry
from typing import Optional, List

@strawberry.type
class lugar:
    id: Optional[str] = None
    userID: Optional[str] = None
    establishmentName: Optional[str]
    opening: Optional[str] = None
    closing: Optional[str] = None
    establishmentType: Optional[str]
    capacity: Optional[int]
    description: Optional[str]
    # menu: Optional[str] = None
    coverPicture: Optional[str] = None
    location: Optional[str]
    city: Optional[int] = None
    bookings: Optional[int] = None