import strawberry
from typing import Optional, List
from reportes.type_def.Tutorias_td import tutoria, tutoria_input
from reportes.type_def.Obs_td import obs, obs_input
from reportes.type_def.Rems_td import rems, rems_input

@strawberry.type
class reportes:
    usuario_estudiante0: str
    usuario_tutor0: str
    programa: str
    departamento: str
    facultad: str
    _id: Optional[str] =None
    nombre_form: str
    nivel: str
    documento: int
    tipologia: str
    #tutorias
    usuario_estudiante: str
    usuario_tutor: str
    estado_tutor: str
    fecha: str

    lista: Optional[List[tutoria]] =None
    #observaciones
    observaciones: Optional[List[obs]] =None
    #remisiones
    remisiones: Optional[List[rems]] = None

@strawberry.input
class reportes_input:
    usuario_estudiante0: str
    usuario_tutor0: str
    programa: str
    departamento: str
    facultad: str
    _id: Optional[str] =None
    nombre_form:  str
    nivel: str
    documento: int
    tipologia: str
    #tutorias
    usuario_estudiante: str
    usuario_tutor: str
    estado_tutor: str
    fecha: str

    lista: Optional[List[tutoria_input]] = None
    #observaciones
    observaciones: Optional[List[obs_input]] = None
    #Remisiones
    remisiones: Optional[List[rems_input]] = None