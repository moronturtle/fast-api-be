import os

import strawberry
from strawberry.fastapi import GraphQLRouter

from app.api.graphql.root_mutation import Mutation
from app.api.graphql.root_query import Query

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, graphiql=(ENVIRONMENT == "development"))
