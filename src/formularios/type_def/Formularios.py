import strawberry
from typing import List, Optional
from formularios.type_def.Respuesta import respuesta, respuesta_input
from formularios.type_def.AR_Preguntasrespuestas import preguntasrespuestas as xx, preguntasrespuestas_input

@strawberry.type
class formulario:
    documento: str
    nombre: str
    apellido: str
    usuarioun: Optional[str]
    fechacreacion: str
    idform: str
    tipologia: str
    respuestas: Optional[List[respuesta]]=None
    preguntasrespuestas: Optional[List[xx]]=None

@strawberry.input
class formulario_input:
    documento: str
    nombre: str
    apellido: str
    usuarioun: Optional[str]
    fechacreacion: str
    idform: str
    tipologia: str
    respuestas: Optional[List[respuesta_input]]=None   
    preguntasrespuestas: Optional[List[preguntasrespuestas_input]] =None







