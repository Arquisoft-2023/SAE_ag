import strawberry
import requests
from dacite import from_dict

# from strawberry.types import Info
from gestionUsuarios.Server import url, port
from gestionUsuarios.type_def.gestionUsuarios_td import *
import typing
from gestionUsuarios.utilities import *



entryPoint = "bienestar"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class Query:
    
    #Usuarios

    @strawberry.field
    def leer_usuarios(self) -> typing.List[UsuarioEsquema]:
        response = requests.request("GET", f'{urlApi}/usuarios')
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "lista")
    
    @strawberry.field
    def buscar_un_usuario(self, usuario_un_a_buscar: str) -> UsuarioEsquema: 
        response = requests.request("GET", f'{urlApi}/usuarios/%7Busuario_un%7D?usuario_un_a_buscar={usuario_un_a_buscar}')
        print(response.json())
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")

    #Roles

    @strawberry.field
    def leer_roles(self) -> typing.List[RolEsquema]:
        response = requests.request("GET", f'{urlApi}/usuariosRol')
        return gestion.gestionar_respuesta_micro(self, response, RolEsquema, "lista")

    #UsuariosRoles

    @strawberry.field
    def leer_usuarios_roles(self) -> typing.List[UsuarioRolEsquema]:
        response = requests.request("GET", f'{urlApi}/usuariosRoles/usuariosRol')
        return gestion.gestionar_respuesta_micro(self, response, UsuarioRolEsquema, "lista")
    
    #Departamentos

@strawberry.type
class Mutation:

    #Usuarios

    @strawberry.mutation
    async def ingresar_usuario(self, item: UsuarioEsquemaInput) -> UsuarioEsquema:
        data = mapper_general.to_json(self, item)
        response = requests.post(f'{urlApi}/usuarios', json=data)
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
    
    @strawberry.mutation
    async def modificar_estado_usuario(self, usuario_un_a_buscar: str, estado_nuevo: bool) -> UsuarioEsquema:
        response = requests.request("PUT", f'{urlApi}/usuarios/%7Busuario_un%7D&%7Bestado%7D?usuario_un_a_buscar={usuario_un_a_buscar}&estado_nuevo={estado_nuevo}')
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
    
    @strawberry.mutation
    async def modificar_datos_usuario(self, item: UsuarioEsquemaInput) -> UsuarioEsquema:
        datos_nuevos= mapper_general.to_json(self, item)
        response = requests.put(f'{urlApi}/usuarios/%7Busuario_un%7D?usuario_un_a_econtrar={datos_nuevos["usuario_un"]}', json=datos_nuevos)
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_usuario(self, usuario_un_a_buscar: str) -> typing.List[UsuarioEsquema]:
        response = requests.delete(f'{urlApi}/usuarios/%7Busuario_un%7D?usuario_un_a_econtrar={usuario_un_a_buscar}')
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "lista")

    #Roles

    @strawberry.mutation
    async def ingresar_rol(self, rol : str) -> typing.List[RolEsquema]:
        response = requests.post(f'{urlApi}/usuariosRol?nuevo_rol={rol}')
        return gestion.gestionar_respuesta_micro(self, response, RolEsquema, "lista")
    
    @strawberry.mutation
    async def modificar_nombre_rol(self, rol_a_buscar: str, rol_nuevo: str) -> RolEsquema:
        response = requests.put(f'{urlApi}/usuariosRol/%7Brol_id%7D?rol_a_econtrar={rol_a_buscar}&datos_nuevo_rol={rol_nuevo}')
        return gestion.gestionar_respuesta_micro(self, response, RolEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_rol(self, rol_a_buscar: str) -> typing.List[RolEsquema]:
        response = requests.delete(f'{urlApi}/usuariosRol/%7Brol_id%7D?rol_a_econtrar={rol_a_buscar}')
        return gestion.gestionar_respuesta_micro(self, response, RolEsquema, "lista")
    
    #UsuariosRoles
    @strawberry.mutation
    async def asignar_rol_a_usuario(self, usuario_un_a_buscar: str, rol_a_buscar: str) -> typing.List[UsuarioRolEsquema]:
        response = requests.post(f'{urlApi}/usuariosRoles/%7Busuario_un%7D&%7Brol_id%7D?usuario_un_a_buscar={usuario_un_a_buscar}&rol_id_a_buscar={rol_a_buscar}')
        return gestion.gestionar_respuesta_micro(self, response, UsuarioRolEsquema, "lista")
    
    @strawberry.mutation
    async def eliminar_usuario_y_rol(self, usuario_un_a_buscar: str) -> str:
        response = requests.delete(f'{urlApi}/usuariosRoles/usuariosRol/%7Busuario_un%7D?usuario_un_elim={usuario_un_a_buscar}')
        return response
    
    @strawberry.mutation
    async def modificar_usuario_y_rol(self, usuario_un: str, rol_nuevo: str) -> str:
        response = requests.put(f'{urlApi}/usuariosRoles/usuariosRol/%7Busuario_un%7D&%7Brol_id%7D?usuario_un_a_buscar={usuario_un}&rol_id_nuevo={rol_nuevo}')
        return response
    
    #Departamentos

   