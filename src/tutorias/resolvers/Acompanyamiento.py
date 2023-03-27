import strawberry
import requests
import json

# from strawberry.types import Info
from tutorias.Server import url, port

entryPoint = "acompanyamiento"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class Query:
    @strawberry.field
    def test(self) -> str:
        return "Acompanyamiento"
    
    @strawberry.field
    def all(self) -> str:
        response = requests.request("GET", f'{urlApi}/all')
        data = json.dumps(response.json())
        # print(data[0])
        return data
        # return "Probando"
