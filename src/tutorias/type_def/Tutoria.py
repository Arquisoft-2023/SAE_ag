import strawberry
from typing import Optional

@strawberry.type
class tutoria:
    _id: Optional[str] = None
    fecha: str
    lugar: str
    estado: str
    objetivo: Optional[str] = None
    acuerdo: Optional[str] = None
    observaciones_tutor: Optional[str] = None
    observaciones_estudiante: Optional[str] = None

@strawberry.input
class tutoria_input:
    _id: Optional[str] = None
    fecha: str
    lugar: str
    estado: str
    objetivo: Optional[str] = None
    acuerdo: Optional[str] = None
    observaciones_tutor: Optional[str] = None
    observaciones_estudiante: Optional[str] = None