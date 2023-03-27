import strawberry

@strawberry.type
class acompanyamiento:
    _id: str
    usuario_un_estudiante: str
    usuario_un_tutor: str
    es_tutor: str


