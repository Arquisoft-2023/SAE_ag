import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from autenticacion.resolvers.autenticacion_rs import Query, Mutation

autenticacion= APIRouter()

schema_autenticacion = strawberry.Schema(Query,Mutation)
# schema_observacion = strawberry.Schema(query, mutation)
# schema_tutoria = strawberry.Schema(query, mutation)

graphql_app_autenticacion = GraphQL(schema_autenticacion)
# graphql_app_observacion = GraphQL(schema_observacion)
# graphql_app_tutoria = GraphQL(schema_tutoria)


autenticacion.add_route("/signin", graphql_app_autenticacion)
# tutorias.add_route("/observacion", graphql_app_observacion)
# tutorias.add_route("/tutoria", graphql_app_tutoria)