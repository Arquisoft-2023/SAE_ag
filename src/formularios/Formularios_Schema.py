import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from formularios.resolvers.formularios import Query_formularios, Mutation_formularios
from formularios.resolvers.tamizajes import Query_tamizajes, Mutation_formularios

formularios = APIRouter()

schema_formulario = strawberry.Schema(Query_formularios,  Mutation_formularios)
schema_tamizajes = strawberry.Schema(Query_tamizajes, Mutation_formularios)
# schema_tutoria = strawberry.Schema(query, mutation)

graphql_app_formulario = GraphQL(schema_formulario)
graphql_app_tamizajes = GraphQL(schema_tamizajes)
# graphql_app_tutoria = GraphQL(schema_tutoria)


formularios.add_route("/formularios", graphql_app_formulario)
formularios.add_route("/tamizajes", graphql_app_tamizajes)
# tutorias.add_route("/tutoria", graphql_app_tutoria)