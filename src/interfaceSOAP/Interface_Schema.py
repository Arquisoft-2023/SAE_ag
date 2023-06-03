import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from interfaceSOAP.resolvers.Consume1C import query

interface = APIRouter()

schema_interface = strawberry.Schema(query)

graphql_app_interface = GraphQL(schema_interface)


interface.add_route("/consume/1C", graphql_app_interface)