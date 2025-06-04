import strawberry
from typing import List
from app.api.graphql.types.category_type import CategoryType
from app.api.graphql.resolvers.category_resolver import resolve_all_categories, resolve_category_by_id

def all_categories_resolver() -> List[CategoryType]:
    categories = resolve_all_categories()
    return [CategoryType(id=cat.id, category=cat.category) for cat in categories]

def category_by_id_resolver(id: str) -> CategoryType:
    cat = resolve_category_by_id(id)
    return CategoryType(id=cat.id, category=cat.category)

@strawberry.type
class CategoryQuery:
    all_categories: List[CategoryType] = strawberry.field(resolver=all_categories_resolver)
    category_by_id: CategoryType = strawberry.field(resolver=category_by_id_resolver)
