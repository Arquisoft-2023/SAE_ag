# from strawberry.types import Info
import strawberry
import requests
import typing

from tutorias.Server import url, port
from tutorias.type_def.Acompanyamiento import acompanyamiento, acompanyamiento_input
from tutorias.utilities import mapper, error

entryPoint = "acompanyamiento"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class Query:
    @strawberry.field
    def test(self) -> str:
        return "Acompanyamiento"
    
    @strawberry.field
    def obtener_acompanyamiento(self) -> typing.List[acompanyamiento]: 
        response = requests.request("GET", f'{urlApi}/all')
        return error.gestionar_respuesta_micro(self, response, acompanyamiento, "lista")
     
    @strawberry.field
    def obtener_tutor(self, usuario_un_estudiante: str) -> str: 
        response = requests.request("GET", f'{urlApi}/{usuario_un_estudiante}')
        return error.gestionar_respuesta_micro(self, response, key="usuario_un_tutor")
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def asignar_tutor(self, item: acompanyamiento_input) -> acompanyamiento:
        response = requests.request("POST", f'{urlApi}/asignar', json=mapper.to_json(self, item, "asignar"))
        return error.gestionar_respuesta_micro(self, response, acompanyamiento, "uno")
