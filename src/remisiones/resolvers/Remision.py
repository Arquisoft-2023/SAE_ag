# from strawberry.types import Info
import strawberry
import requests
import typing

from remisiones.Server import url, port
from remisiones.type_def.remisiones_td import *
from remisiones.utilities import *

entryPoint = ""
urlApi = f'http://{url}:{port}{entryPoint}'

@strawberry.type
class Query:
    
    @strawberry.field
    def test(self) -> str:
        return "Remisiones API GATEWAY Working!"    
    
    #Tipos de Remision
    
    @strawberry.field
    def obtener_tiposRemision(self) -> typing.List[TiposRemision]:
        response = requests.request("GET", f'{urlApi}/tipo_remision/lista')
        print(response.json())
        return gestion.gestionar_respuesta_micro(self, response, TiposRemision,"lista")
    
    #Solicitudes de Remision
    
    @strawberry.field
    def obtener_solicitudesRemision(self) -> typing.List[SolicitudesRemision]:
        response = requests.request("GET", f'{urlApi}/solicitud_remision/lista')
        print(response.json())
        return gestion.gestionar_respuesta_micro(self, response, SolicitudesRemision,"lista")
    
    #Primeras Escuchas
    
    @strawberry.field
    def obtener_primerasEscuchas(self) -> typing.List[PrimerasEscuchas]:
        response = requests.request("GET", f'{urlApi}/primera_escucha/lista')
        return gestion.gestionar_respuesta_micro(self, response, PrimerasEscuchas,"lista")
    
    #Remisiones
    
    @strawberry.field
    def obtener_remisiones(self) -> typing.List[Remisiones]:
        response = requests.request("GET", f'{urlApi}/remision/lista')
        return gestion.gestionar_respuesta_micro(self, response, Remisiones,"lista")
    
    @strawberry.field
    def obtener_remisiones_un_usuario(self, usuarioUn: str) -> typing.List[Remisiones]: 
        response = requests.request("GET", f'{urlApi}/remision/listaUsuarioUn/{usuarioUn}')
        print(response.json())
        return gestion.gestionar_respuesta_micro(self, response, Remisiones, "lista")
    
    @strawberry.field
    def obtener_remisiones_efectivas(self) -> typing.List[Remisiones]:
        response = requests.request("GET",f'{urlApi}/remision/listaRemisionesEfectivas')
        return gestion.gestionar_respuesta_micro(self, response, Remisiones, "lista")
    

@strawberry.type
class Mutation:
    
    #Solicitudes de Remision
    
    @strawberry.mutation
    async def generarSolicitud(self, item: NuevaSolicitudRemisionInput) -> NuevaSolicitudRemision:
        data = mapper_remision.to_json(self, item)
        print(data)
        response = requests.post(f'{urlApi}/solicitud_remision/crear', json=data)
        print(response.json())
        print(response.status_code)
        return gestion.gestionar_respuesta_micro(self, response,NuevaSolicitudRemision, "uno")
    
    @strawberry.mutation
    async def eliminar_solicitud(self, id: int) -> str:
        response = requests.delete(f'{urlApi}/solicitud_remision/eliminar/{id}')
        return gestion.gestionar_respuesta_micro(self, response, "boolean")
    
    #Remisiones
    
    @strawberry.mutation
    async def generarRemision(self, item: NuevaRemisionInput) -> NuevaRemision:
        data = mapper_remision.to_json(self, item)
        response = requests.post(f'{urlApi}/remision/crear', json=data)
        return gestion.gestionar_respuesta_micro(self, response,NuevaRemision, "uno")
    
    @strawberry.mutation
    async def eliminar_remision(self, id: int) -> str:
        response = requests.delete(f'{urlApi}/remision/eliminar/{id}')
        return gestion.gestionar_respuesta_micro(self, response, "boolean")
    
    #Primeras Escuchas
    
    @strawberry.mutation
    async def modificarPrimeraEscucha(self, id: int, item: PrimeraEscuchaInput) -> str:
        data = mapper_remision.to_json(self, item)
        response = requests.put(f'{urlApi}/remision/primeraEscucha/{id}', json=data)
        return gestion.gestionar_respuesta_micro(self,response, "boolean")
    
        