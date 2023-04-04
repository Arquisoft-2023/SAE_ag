import strawberry
import requests
import json

# from strawberry.types import Info
from tutorias.Server import url, port
from tutorias.type_def.Acompanyamiento import acompanyamiento
import typing

entryPoint = "acompanyamiento"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class Query:
    @strawberry.field
    def test(self) -> str:
        return "Acompanyamiento"
    
    @strawberry.field
    def all(self) -> str: 
        reponse = requests.request("GET", f'{urlApi}/all')
        print(reponse.json())
        data = reponse.json()
        # data = json(data)
        # print(type(data[0]['_id']))
        # print(data[0]['_id'])
        return reponse
        # return "Probando"
