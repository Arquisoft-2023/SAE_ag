import strawberry
from typing import Optional

@strawberry.type
class tutoria:
    _id: Optional[str] = None
    fecha: str
    lugar: str
    estado: str
    objetivo: Optional[str] = ""
    acuerdo: Optional[str] = ""
    observaciones_tutor: Optional[str] = ""
    observaciones_estudiante: Optional[str] = ""

@strawberry.input
class tutoria_input:
    _id: Optional[str] = None
    fecha: str
    lugar: str
    estado: str
    objetivo: Optional[str] = ""
    acuerdo: Optional[str] = ""
    observaciones_tutor: Optional[str] = ""
    observaciones_estudiante: Optional[str] = ""