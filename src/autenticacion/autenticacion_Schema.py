import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from autenticacion.resolvers.autenticacion_rs import Query, Mutation

autenticacion= APIRouter()

schema_autenticacion = strawberry.Schema(Query,Mutation)

graphql_app_autenticacion = GraphQL(schema_autenticacion)


autenticacion.add_route("/signin", graphql_app_autenticacion)