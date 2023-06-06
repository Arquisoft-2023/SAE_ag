import strawberry
import requests
import typing

from autenticacion.Server import url, port
from autenticacion.type_def.autenticacion_td import UsuarioAuthInput, UsuarioAuthWithToken, UsuarioAuthGeneral
from autenticacion.utilities import gestion, mapper_general
from gestionUsuarios.resolvers.gestionUsuarios_rs import Query as gestionUsuariosQuery, Mutation as gestionUsuariosMutation

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
    async def signin(self, item: UsuarioAuthInput) -> any:
        userInGestionUsuarios = gestionUsuariosQuery.buscar_un_usuario(self, usuario_un_a_buscar = item.usuario_un)
        if userInGestionUsuarios:
            data = {'usuario_un': item.usuario_un, 'password': item.password }
            url = f'{urlApi}/signin'
            response = requests.post(url, data=data)
            return gestion.gestionar_respuesta_micro(self, response, UsuarioAuthWithToken, "uno")
        else:
            return {'msg' : "Usuario inexistente"}
    # @strawberry.mutation
    # async def signin(self, usuario_un: str, password: str) -> str:
    #     url = f'{urlApi}/signin'
    #     data = {'usuario_un': usuario_un, 'password': password}

    #     response = requests.post(url, data=data)
    #     content = response.text

    #     return content
    #async def signin(self, item: UsuarioAuthInput):
        
        # ldapAuthMS = requests.request("POST", f'{urlApi}/signin', json=mapper_general.to_json(self, UsuarioAuthInput))
        # return ldapAuthMS
        # userInGestionUsuarios = gestionUsuariosQuery.buscar_un_usuario(self, usuario_un_a_buscar = item.usuario_un)
        # if userInGestionUsuarios:
        #     ldapAuthMS = requests.request("POST", f'{urlApi}/signin', json=mapper_general.to_json(self, UsuarioAuthInput))
        #     ldapAuthMSToken = ldapAuthMS.token
        #     if ldapAuthMS and ldapAuthMSToken:
        #         if item.tokentype == "web":
        #             gestionMSTokenWeb = gestionUsuariosMutation.modificar_token_usuario_web(self, usuario_web = item.usuario_un, token_nuevo = ldapAuthMSToken)
        #             return gestionMSTokenWeb
        #         if item.tokentype == "movil":
        #             gestionMSTokenMovil = gestionUsuariosMutation.modificar_token_usuario_movil(self, usuario_movil = item.usuario_un, token_nuevo = ldapAuthMSToken)
        #             return gestionMSTokenMovil
        #     else:    
        #         return None
        # else:
        #     return None


    @strawberry.mutation
    async def signout(self) -> UsuarioAuthGeneral:
         responseOut = requests.request("PUT", f'{urlApi}/signout')
         return gestion.gestionar_respuesta_micro(self, responseOut, UsuarioAuthGeneral, "uno")