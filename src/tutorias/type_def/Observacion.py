import strawberry

@strawberry.type
class observacion:
    _id: str
    fecha: str
    descripcion: str