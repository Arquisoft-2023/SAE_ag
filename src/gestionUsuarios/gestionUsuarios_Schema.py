import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from gestionUsuarios.resolvers.gestionUsuarios_rs import Query, Mutation

gestionUsuarios = APIRouter()

schema_gestionUsuarios = strawberry.Schema(Query,Mutation)
# schema_observacion = strawberry.Schema(query, mutation)
# schema_tutoria = strawberry.Schema(query, mutation)

graphql_app_gestionUsuarios = GraphQL(schema_gestionUsuarios)
# graphql_app_observacion = GraphQL(schema_observacion)
# graphql_app_tutoria = GraphQL(schema_tutoria)


gestionUsuarios.add_route("/usuarios", graphql_app_gestionUsuarios)
# tutorias.add_route("/observacion", graphql_app_observacion)
# tutorias.add_route("/tutoria", graphql_app_tutoria)