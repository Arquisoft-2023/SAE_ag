import strawberry
from typing import Optional, List
from tutorias.type_def.Tutoria import tutoria
from tutorias.type_def.Observacion import observacion

@strawberry.type
class acompanyamiento:
    id: str
    usuario_un_estudiante: str
    usuario_un_tutor: str
    es_tutor: str
    #lista_tutoria: Optional[List[tutoria]] = None
    #lista_observacion: Optional[List[observacion]] = None
