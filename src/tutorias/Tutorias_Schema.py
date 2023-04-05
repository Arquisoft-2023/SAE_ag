import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from tutorias.resolvers.Acompanyamiento import Query, Mutation

tutorias = APIRouter()

schema_acompanyamiento = strawberry.Schema(Query, Mutation)
# schema_observacion = strawberry.Schema(query, mutation)
# schema_tutoria = strawberry.Schema(query, mutation)

graphql_app_acompanyamiento = GraphQL(schema_acompanyamiento)
# graphql_app_observacion = GraphQL(schema_observacion)
# graphql_app_tutoria = GraphQL(schema_tutoria)


tutorias.add_route("/acompanyamiento", graphql_app_acompanyamiento)
# tutorias.add_route("/observacion", graphql_app_observacion)
# tutorias.add_route("/tutoria", graphql_app_tutoria)