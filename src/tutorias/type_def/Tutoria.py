import strawberry

@strawberry.type
class tutoria:
    _id: str
    fecha: str
    lugar: str
    estado: str
    objetivo: str
    acuerdo: str
    observaciones_tutor: str
    observaciones_estudiante: str