import strawberry

@strawberry.type
class tutoria:
    lugar: str
    estado: str
    objetivo: str
    acuerdo: str

@strawberry.input
class tutoria_input:
    lugar: str
    estado: str
    objetivo: str
    acuerdo: str