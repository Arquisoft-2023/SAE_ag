import strawberry
from typing import List, Optional
from formularios.type_def.Respuestas import respuestas, respuestas_input

@strawberry.type
class respuesta:
    rdocumento: str
    rapellido: str
    fecharealizacion: str
    rusuarioun: str
    rnombre:str
    respuestas: List[respuestas]

@strawberry.input
class respuesta_input:
    rdocumento: str
    rapellido: str
    fecharealizacion: str
    rusuarioun: str
    rnombre:str
    respuestas: List[respuestas_input]    