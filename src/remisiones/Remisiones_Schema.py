import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from remisiones.resolvers.Remision import Query

remisiones = APIRouter()

schema_remision = strawberry.Schema(Query)
# schema_observacion = strawberry.Schema(query, mutation)
# schema_tutoria = strawberry.Schema(query, mutation)

graphql_app_remisiones = GraphQL(schema_remision)
# graphql_app_observacion = GraphQL(schema_observacion)
# graphql_app_tutoria = GraphQL(schema_tutoria)


remisiones.add_route("/remisiones", graphql_app_remisiones)
# tutorias.add_route("/observacion", graphql_app_observacion)
# tutorias.add_route("/tutoria", graphql_app_tutoria)