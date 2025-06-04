import strawberry

from app.api.graphql.queries.category_query import CategoryQuery


@strawberry.type
class Query(CategoryQuery):
    pass
