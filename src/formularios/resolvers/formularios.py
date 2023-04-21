import strawberry
import requests
import json
import typing
from dacite import from_dict
from formularios.utilities import gestion, mapper_formulario

# from strawberry.types import Info
from formularios.Server import url, port
from formularios.type_def.Formularios import formulario, formulario_input

entryPoint = "formularios"
urlApi = f'http://{url}:{port}/{entryPoint}/'


@strawberry.type
class Query_formularios:
    @strawberry.field
    def test(self) -> str:
        return "Acompanyamiento"
    
    @strawberry.field
    def formularios(self) ->  typing.List[formulario]:
        response = requests.request("GET", f'{urlApi}')
        return gestion.gestionar_respuesta_micro(self, response, formulario, "lista")
    

        
    @strawberry.field
    def formulario(self, id: str) -> formulario:
        response = requests.request("GET", f'{urlApi}id/{id}')
        return gestion.gestionar_respuesta_micro(self, response, formulario, "uno")
    
@strawberry.type
class Mutation_formularios:
    @strawberry.mutation
    async def crear_formulario(self, item: formulario_input) -> formulario:
        response = requests.request("POST", f'{urlApi}crear/', json=mapper_formulario.to_json(self, item, "crear_form"))
        return gestion.gestionar_respuesta_micro(self, response, formulario, "uno")
    
 
    @strawberry.mutation
    async def actualizar_form(self,id:str, item: formulario_input) -> formulario:
        response = requests.request("PUT", f'{urlApi}actua/{id}', json=mapper_formulario.to_json(self, item, metodo="todo_form"))
        return gestion.gestionar_respuesta_micro(self, response, formulario, "uno")
    
    @strawberry.mutation
    async def borrarform(self,id:str) -> str:
        response = requests.request("DELETE", f'{urlApi}borrar/{id}')
        return (response)
    
