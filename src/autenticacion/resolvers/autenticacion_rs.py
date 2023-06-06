import strawberry
import requests
import typing
import json

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
    async def signin(self, usuario_un: str, password: str, tokentype: str) -> UsuarioAuthWithToken:
        userInGestionUsuarios = gestionUsuariosQuery.buscar_un_usuario(self, usuario_un_a_buscar = usuario_un)
        returnBad = UsuarioAuthWithToken(ldapRes="Error", usuario_un="Error", token="Error")
        if userInGestionUsuarios:
            data = {'usuario_un': usuario_un, 'password': password }
            url = f'{urlApi}/signin'
            response = requests.post(url, data=data)
            content = response.text
            # Analizar la cadena JSON en "content"
            response_data = json.loads(content)
            if response_data and response_data['ldapRes'] == "true":
                if tokentype == "web":
                    gestionUsuariosMutation.modificar_token_usuario_web(self, usuario_web = usuario_un, token_nuevo = response_data['token'])
                if tokentype == "movil":
                    gestionUsuariosMutation.modificar_token_usuario_movil(self, usuario_movil = usuario_un, token_nuevo = response_data['token'])
            return UsuarioAuthWithToken(ldapRes=response_data['ldapRes'], usuario_un=response_data['usuario_un'], token=response_data['token'])
            
        else:
            return returnBad

    @strawberry.mutation
    async def signout(self) -> UsuarioAuthGeneral:
         responseOut = requests.request("PUT", f'{urlApi}/signout')
         return gestion.gestionar_respuesta_micro(self, responseOut, UsuarioAuthGeneral, "uno")