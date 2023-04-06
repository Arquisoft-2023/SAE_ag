# from strawberry.types import Info
import strawberry
import requests
import typing

from tutorias.Server import url, port
from tutorias.type_def.Acompanyamiento import acompanyamiento_input
from tutorias.utilities import gestion, mapper_tutoria

entryPoint = "observacion"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class query_observacion:
    @strawberry.field
    def test(self) -> str:
        return "Observacion"

@strawberry.type
class mutation_observacion:
    @strawberry.mutation
    async def crear_obs(self, item: acompanyamiento_input) -> str:
        response = requests.request("POST", f'{urlApi}/crear', json=mapper_tutoria.to_json(self, item, metodo="crear_obs"))
        return gestion.gestionar_respuesta_micro(self, response, tipo_respuesta="boolean")
