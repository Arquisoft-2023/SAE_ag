import strawberry
import requests
import typing
import json

from reportes.Server import url,port
from reportes.type_def.Reportes_td import reportes, reportes_input
from reportes.utilities import gestion, mapper_general, mapper_repor

entryPoint = "repo"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class Query:
    @strawberry.field
    def test(self) -> str:
        return "reportes"
    
    @strawberry.field
    def obtener_reportes(self) -> typing.List[reportes]: 
        response = requests.request("GET", f'{urlApi}')
        return gestion.gestionar_respuesta_micro(self, response, reportes, "lista")

    @strawberry.field
    def obtener_estudiante(self) -> typing.List[reportes]: 
        response = requests.request("GET", f'{urlApi}/data/estudiante?usuario_estudiante={usuario_estudiante}')
        return gestion.gestionar_respuesta_micro(self, response, reportes, "lista")
    
@strawberry.type
class Mutation:
    #@strawberry.mutation
    #async def add_reporte(self, item: reportes_input) -> reportes:
     #   response = requests.request("POST", f'{urlApi}/repo', json= mapper_general.to_json(self, item ))
      #  return gestion.gestionar_respuesta_micro(self, response, reportes,  "lista")

    @strawberry.mutation
    async def add_reporte(self, item: reportes_input) -> reportes:
        data = mapper_repor.to_json(self, item)
        response = requests.post(f'{urlApi}', json=data)
        return gestion.gestionar_respuesta_micro(self, response, reportes, "lista")