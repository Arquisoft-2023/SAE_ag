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
        return "remision"
    
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
    
        
                                 
