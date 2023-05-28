import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from gestionUsuarios.resolvers.gestionUsuarios_rs import Query, Mutation

gestionUsuarios = APIRouter()

schema_gestionUsuarios = strawberry.Schema(Query,Mutation)

graphql_app_gestionUsuarios = GraphQL(schema_gestionUsuarios)

gestionUsuarios.add_route("/usuarios", graphql_app_gestionUsuarios)