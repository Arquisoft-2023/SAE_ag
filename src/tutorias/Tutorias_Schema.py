import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from tutorias.resolvers.Acompanyamiento import query_acompanyamiento, mutation_acompanyamiento
from tutorias.resolvers.Observacion import query_observacion, mutation_observacion
from tutorias.resolvers.Tutoria import query_tutoria, mutation_tutoria

tutorias = APIRouter()

schema_acompanyamiento = strawberry.Schema(query_acompanyamiento, mutation_acompanyamiento)
schema_observacion = strawberry.Schema(query_observacion, mutation_observacion)
schema_tutoria = strawberry.Schema(query_tutoria, mutation_tutoria)

graphql_app_acompanyamiento = GraphQL(schema_acompanyamiento)
graphql_app_observacion = GraphQL(schema_observacion)
graphql_app_tutoria = GraphQL(schema_tutoria)


tutorias.add_route("/acompanyamiento", graphql_app_acompanyamiento)
tutorias.add_route("/observacion", graphql_app_observacion)
tutorias.add_route("/tutoria", graphql_app_tutoria)