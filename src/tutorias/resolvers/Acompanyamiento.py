# from strawberry.types import Info
import strawberry
import requests
import typing

from tutorias.Server import url, port
from tutorias.type_def.Acompanyamiento import acompanyamiento, acompanyamiento_input
from tutorias.utilities import gestion, mapper_tutoria

entryPoint = "acompanyamiento"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class query_acompanyamiento:
    @strawberry.field
    def test(self) -> str:
        return "Acompanyamiento"
    
    @strawberry.field
    async def obtener_acompanyamiento(self) -> typing.List[acompanyamiento]: 
        response = requests.request("GET", f'{urlApi}/all')
        return gestion.gestionar_respuesta_micro(self, response, acompanyamiento, "lista")

    @strawberry.field
    def obtener_acompanyamiento_uno(self, item: acompanyamiento_input) -> typing.List[acompanyamiento]:
        response = requests.request("GET", f'{urlApi}/one', json=mapper_tutoria.to_json(self, item))
        return gestion.gestionar_respuesta_micro(self, response, acompanyamiento,  "lista")
    
    @strawberry.field
    def obtener_acompanyamiento_tutor(self, usuario_un_tutor: str) -> typing.List[acompanyamiento]: 
        response = requests.request("GET", f'{urlApi}/listaTutor/{usuario_un_tutor}')
        return gestion.gestionar_respuesta_micro(self, response, acompanyamiento, "lista")
     
    @strawberry.field
    def obtener_tutor(self, usuario_un_estudiante: str) -> str: 
        response = requests.request("GET", f'{urlApi}/{usuario_un_estudiante}')
        return gestion.gestionar_respuesta_micro(self, response, tipo_respuesta="uno_con_key", key="usuario_un_tutor")
    
    @strawberry.field
    def obtener_tutores(self) -> typing.List[str]: 
        response = requests.request("GET", f'{urlApi}/tutores')
        return gestion.gestionar_respuesta_micro(self, response)
    
    @strawberry.field
    def obtener_estudiantes(self, usuario_un_tutor: str) -> typing.List[acompanyamiento]: 
        response = requests.request("GET", f'{urlApi}/estudiantes/{usuario_un_tutor}')
        return gestion.gestionar_respuesta_micro(self, response, acompanyamiento, "lista")
    
@strawberry.type
class mutation_acompanyamiento:
    @strawberry.mutation
    async def asignar_tutor(self, item: acompanyamiento_input) -> acompanyamiento:
        response = requests.request("POST", f'{urlApi}/asignar', json=mapper_tutoria.to_json(self, item, "asignar"))
        return gestion.gestionar_respuesta_micro(self, response, acompanyamiento,  "uno")

    @strawberry.mutation
    async def actualizar_tutor(self, item: acompanyamiento_input) -> str:
        response = requests.request("PUT", f'{urlApi}/actualizar', json=mapper_tutoria.to_json(self, item, "asignar"))
        return gestion.gestionar_respuesta_micro(self, response, tipo_respuesta="boolean")
