# from strawberry.types import Info
import strawberry
import requests
import typing

from interfaceSOAP.Server import url, port
from interfaceSOAP.type_def.Lugar import lugar
from interfaceSOAP.utilities import gestion

entryPoint = "consumo/1C"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class query:
    @strawberry.field
    def test(self) -> str:
        return "Interface OK"
    
    @strawberry.field
    async def obtener_lugares_1C(self) -> typing.List[lugar]: 
        response = requests.request("GET", f'{urlApi}')
        return gestion.gestionar_respuesta_micro(self, response, lugar, "lista") 