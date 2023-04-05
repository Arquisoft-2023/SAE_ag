import strawberry
import requests
from dacite import from_dict

# from strawberry.types import Info
from gestionUsuarios.Server import url, port
from gestionUsuarios.type_def.gestionUsuarios_td import *
import typing
from gestionUsuarios.utilities import mapper, error



entryPoint = "bienestar"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class Query:
    
    #Usuarios

    @strawberry.field
    def leer_usuarios(self) -> typing.List[UsuarioEsquema]:
        response = requests.request("GET", f'{urlApi}/usuarios')
        return error.gestionar_respuesta_micro(self, response, UsuarioEsquema, "lista")
    
    @strawberry.field
    def buscar_un_usuario(self, usuario_un_a_buscar: str) -> UsuarioEsquema: 
        response = requests.request("GET", f'{urlApi}/usuarios/%7Busuario_un%7D?usuario_un_a_buscar={usuario_un_a_buscar}')
        print(response.json())
        return error.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")

@strawberry.type
class Mutation:

    #Usuarios

    @strawberry.mutation
    async def ingresar_usuario(self, item: UsuarioEsquemaInput) -> UsuarioEsquema:
        response = requests.request("POST", f'{urlApi}/usuarios', json=mapper.to_json(self, item, "crearUsuario"))
        return error.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
    
    @strawberry.mutation
    async def modificar_estado_usuario(self, usuario_un_a_buscar: str, estado_nuevo: bool) -> UsuarioEsquema:
        response = requests.request("PUT", f'{urlApi}/usuarios/%7Busuario_un%7D&%7Bestado%7D?usuario_un_a_buscar={usuario_un_a_buscar}&estado_nuevo={estado_nuevo}')
        return error.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
    
    @strawberry.mutation
    async def modificar_datos_usuario(self, item: UsuarioEsquemaInput) -> UsuarioEsquema:
        datos_nuevos= mapper.to_json(self, item, "crearUsuario")
        response = requests.put(f'{urlApi}/usuarios/%7Busuario_un%7D?usuario_un_a_econtrar={datos_nuevos["usuario_un"]}', json=datos_nuevos)
        return error.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_usuario(self, usuario_un_a_buscar: str) -> typing.List[UsuarioEsquema]:
        response = requests.delete(f'{urlApi}/usuarios/%7Busuario_un%7D?usuario_un_a_econtrar={usuario_un_a_buscar}')
        return error.gestionar_respuesta_micro(self, response, UsuarioEsquema, "lista")
