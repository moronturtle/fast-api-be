import uuid

import strawberry


@strawberry.type
class CategoryType:
    id: uuid.UUID
    category: str
