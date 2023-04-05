import strawberry
from typing import Optional

@strawberry.type
class observacion:
    _id: Optional[str] = None
    fecha: str
    descripcion: str

@strawberry.input
class observacion_input:
    _id: Optional[str] = None
    fecha: str
    descripcion: str