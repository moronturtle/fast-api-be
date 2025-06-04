import strawberry

from app.api.graphql.resolvers.category_resolver import resolve_create_category
from app.api.graphql.types.category_type import CategoryType


@strawberry.type
class CategoryMutation:
    @strawberry.mutation
    def create_category(self, category: str) -> CategoryType:
        result = resolve_create_category(category)
        return CategoryType(id=result.id, category=result.category)
