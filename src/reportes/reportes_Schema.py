import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL


from reportes.resolvers.Reportes import Query, Mutation

reportes = APIRouter()

schema_reportes = strawberry.Schema(Query,Mutation)
# schema_observacion = strawberry.Schema(query, mutation)
# schema_tutoria = strawberry.Schema(query, mutation)

graphql_app_reportes = GraphQL(schema_reportes)
# graphql_app_observacion = GraphQL(schema_observacion)
# graphql_app_tutoria = GraphQL(schema_tutoria)

reportes.add_route("/repo", graphql_app_reportes)
# tutorias.add_route("/observacion", graphql_app_observacion)
# tutorias.add_route("/tutoria", graphql_app_tutoria)