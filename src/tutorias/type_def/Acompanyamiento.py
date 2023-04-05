import strawberry
from typing import Optional, List
from tutorias.type_def.Tutoria import tutoria, tutoria_input
from tutorias.type_def.Observacion import observacion, observacion_input

@strawberry.type
class acompanyamiento:
    _id: Optional[str] = None
    usuario_un_estudiante: Optional[str]
    usuario_un_tutor: Optional[str]
    es_tutor: Optional[str] = None
    lista_tutoria: Optional[List[tutoria]] = None
    lista_observacion: Optional[List[observacion]] = None


@strawberry.input
class acompanyamiento_input:
    _id: Optional[str] = None
    usuario_un_estudiante: str
    usuario_un_tutor: str
    es_tutor: Optional[str] = None
    lista_tutoria: Optional[List[tutoria_input]] = None
    lista_observacion: Optional[List[observacion_input]] = None