import strawberry
from app.api.graphql.mutations.category_mutation import CategoryMutation

@strawberry.type
class Mutation(CategoryMutation):
    pass
