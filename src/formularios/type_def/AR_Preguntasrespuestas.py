import strawberry
from typing import List, Optional
from formularios.type_def.Posiblesrespuestas import  posiblesrespuestas_input, posiblesrespuestas

@strawberry.type
class preguntasrespuestas:
    pregunta: str
    posiblesrespuestas: Optional[List[posiblesrespuestas]]
    

@strawberry.input
class preguntasrespuestas_input:
    pregunta: str
    posiblesrespuestas: Optional[List[posiblesrespuestas_input]]=None