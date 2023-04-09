import strawberry
import requests
import typing

from autenticacion.Server import url, port
from autenticacion.type_def.autenticacion_td import UsuarioAuthInput, UsuarioAuth, UsuarioAuthWithToken, UsuarioAuthGeneral
from autenticacion.utilities import gestion, mapper_general
from gestionUsuarios.resolvers.gestionUsuarios_rs import Query as gestionUsuariosQuery

entryPoint = "auth"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class Query:
    @strawberry.field
    def test(self) -> str:
        return "Auth API GATEWAY Working!"

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def signin(self, item: UsuarioAuthInput) -> UsuarioAuthWithToken:
        userInGestionUsuarios = gestionUsuariosQuery.buscar_un_usuario(self, usuario_un_a_buscar = item.usuario_un)
        response = requests.request("POST", f'{urlApi}/signin', json=mapper_general.to_json(self, userInGestionUsuarios))
        return gestion.gestionar_respuesta_micro(self, response, UsuarioAuthWithToken, "uno")

    @strawberry.mutation
    async def signout(self) -> UsuarioAuthGeneral:
         responseOut = requests.request("PUT", f'{urlApi}/signout')
         return gestion.gestionar_respuesta_micro(self, responseOut, UsuarioAuthGeneral, "uno")