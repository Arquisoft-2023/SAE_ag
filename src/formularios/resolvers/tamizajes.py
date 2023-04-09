import strawberry
import requests
import json
import typing
from dacite import from_dict
from formularios.utilities import gestion, mapper_formulario

# from strawberry.types import Info
from formularios.Server import url, port
from formularios.type_def.Formularios import formulario, respuesta, formulario_input

entryPoint = "tamizajes"
urlApi = f'http://{url}:{port}/{entryPoint}/'

@strawberry.type
class Query_tamizajes:
    @strawberry.field
    def test(self) -> str:
        return "tamizajes"
    
    @strawberry.field
    def tamizajes(self, id:str) ->  typing.List[respuesta]:
        response = requests.request("GET", f'{urlApi}{id}')
        return gestion.gestionar_respuesta_micro(self, response, respuesta, "lista")
    
    @strawberry.field
    def tamizaje_usuarioun(self, id:str, usuario_un:str) ->  respuesta:
        response = requests.request("GET", f'{urlApi}estudiante/{id}/{usuario_un}')
        return gestion.gestionar_respuesta_micro(self, response, respuesta, "uno")
    
@strawberry.type
class Mutation_formularios:
    @strawberry.mutation
    async def realizar_tamizaje(self,id:str, item: formulario_input) -> str:
        response = requests.request("PUT", f'{urlApi}bienestar/{id}', json=mapper_formulario.to_json(self, item, metodo="todo_form"))
        return (response)