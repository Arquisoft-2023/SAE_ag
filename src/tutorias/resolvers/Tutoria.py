# from strawberry.types import Info
import strawberry
import requests
import asyncio
import threading

from tutorias.type_def.Acompanyamiento import acompanyamiento_input
from tutorias.utilities import gestion, mapper_tutoria
from tutorias.Server import url, port
from tutorias.mq.Client_tutorias import send, go

entryPoint = "tutoria"
urlApi = f'http://{url}:{port}/{entryPoint}'

@strawberry.type
class query_tutoria:
    @strawberry.field
    def test(self) -> str:
        return "Tutoria"
    
    @strawberry.field
    async def testQueue(self) -> str:
        item = "Hola RabbitMQ!"
        response = await go(gestion.gestionar_query(self, item, "testQueue"))
        return gestion.gestionar_respuesta_micro(self, response, data_class="Json", tipo_respuesta="boolean")

@strawberry.type
class mutation_tutoria:
    @strawberry.mutation
    async def crear_tutoria(self, item: acompanyamiento_input) -> str:
        response = requests.request("POST", f'{urlApi}/crear', json=mapper_tutoria.to_json(self, item, metodo="crear_tutoria"))
        return gestion.gestionar_respuesta_micro(self, response, data_class="Json", tipo_respuesta="boolean")

    @strawberry.mutation
    async def actualizar_tutoria_c(self, item: acompanyamiento_input) -> str:
        response = requests.request("PUT", f'{urlApi}/actualizar', json=mapper_tutoria.to_json(self, item, "crear_tutoria"))
        return gestion.gestionar_respuesta_micro(self, response, data_class="Json", tipo_respuesta="boolean")
    
    @strawberry.mutation
    async def crear_tutoria_mq(self, item: acompanyamiento_input) -> str:
        response = await send(gestion.gestionar_query(self, mapper_tutoria.to_json(self, item, metodo="crear_tutoria"), "crear_tutoria"))
        return gestion.gestionar_respuesta_micro(self, response, data_class="Json", tipo_respuesta="boolean")
    
    @strawberry.mutation
    async def actualizar_tutoria_cmq(self, item: acompanyamiento_input) -> str:
        response = await send(gestion.gestionar_query(self, mapper_tutoria.to_json(self, item, metodo="crear_tutoria"), "actualizar_tutoria_c"))
        return gestion.gestionar_respuesta_micro(self, response, data_class="Json", tipo_respuesta="boolean")
