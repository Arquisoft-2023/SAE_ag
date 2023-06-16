import strawberry
import requests
import typing
import json

from autenticacion.Server import url, port
from autenticacion.type_def.autenticacion_td import UsuarioAuthInput, UsuarioAuthWithToken, UsuarioAuthGeneral, TokensVerify
from autenticacion.utilities import gestion, mapper_general
from gestionUsuarios.resolvers.gestionUsuarios_rs import Query as gestionUsuariosQuery, Mutation as gestionUsuariosMutation
from gestionUsuarios.type_def.gestionUsuarios_td import tokenResponse as TokenGestionResponse

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
        userInGestionUsuarios = await gestionUsuariosQuery.buscar_un_usuario(self, usuario_un_a_buscar = usuario_un)
        returnBad = UsuarioAuthWithToken(ldapRes="Error", usuario_un="Error", token="Error")
        if userInGestionUsuarios:
            data = {'usuario_un': usuario_un, 'password': password }
            url = f'{urlApi}/signin'
            response = requests.post(url, data=data)
            content = response.text
            # Analizar la cadena JSON en "content"
            response_data = json.loads(content)
            if tokentype == "web":
                await gestionUsuariosMutation.modificar_token_usuario_web(self, usuario_web = usuario_un, token_nuevo = response_data['token'])
                return UsuarioAuthWithToken(ldapRes=response_data['ldapRes'], usuario_un=response_data['usuario_un'], token=response_data['token'])
            if tokentype == "movil":
                await gestionUsuariosMutation.modificar_token_usuario_movil(self, usuario_movile = usuario_un, token_nuevo = response_data['token'])
                return UsuarioAuthWithToken(ldapRes=response_data['ldapRes'], usuario_un=response_data['usuario_un'], token=response_data['token'])
        else:
            return returnBad

    @strawberry.mutation
    async def signout(self, usuario_un: str) -> TokenGestionResponse:
        if usuario_un:
           return await gestionUsuariosMutation.eliminar_token_usuario_web(self, usuario_web = usuario_un)
    
    @strawberry.mutation
    async def verifyTokens(self, tokenLocalStorage: str, usuario_un: str) -> str:
        tokenDBGestion = await gestionUsuariosQuery.obtener_token_web(self, usuario_un_a_buscar=usuario_un)
        if tokenDBGestion:
            tokenDB = tokenDBGestion.token  # Obtener el valor de la propiedad 'token' del objeto tokenDBGestion
            data = {'tokenDB': tokenDB, 'tokenLocalStorage': tokenLocalStorage}
            url = f'{urlApi}/tokensVerify'
            response = requests.post(url, data=data)
            content = response.text
            return content
            #response_data = json.loads(content)
            # if response_data:
            #     return TokensVerify(TokenDB=response_data['TokenDB'], TokenLocalS=response_data['TokenLocalS'], verify=response_data['verify'])

    @strawberry.mutation
    async def verifyExistenceUserLDAP(self, usuario_un: str) -> bool:
        data = {'usuario_un': usuario_un}
        url = f'{urlApi}/verifyLDAP'
        response = requests.post(url, data=data)
        content = response.text
        response_data = json.loads(content)
        print(response_data)
        if response_data:
            return response_data['ldapRes']