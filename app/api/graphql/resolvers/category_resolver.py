import uuid

import strawberry

from app.db.database import SessionLocal
from app.db.models.categories import Categories
from app.middleware.exceptions import NotFoundException


def resolve_all_categories():
    db = SessionLocal()
    categories = db.query(Categories).all()
    db.close()
    return categories


def resolve_category_by_id(id: str):
    try:
        uuid_obj = uuid.UUID(id)
    except ValueError:
        raise strawberry.exceptions.GraphQLError(f"Format id '{id}' invalid UUID.")

    db = SessionLocal()
    category = db.query(Categories).filter(Categories.id == uuid_obj).first()
    db.close()
    if not category:
        raise strawberry.exceptions.GraphQLError(f"Category with id {id} not found.")
    return category


def resolve_create_category(category: str):
    db = SessionLocal()
    new_category = Categories(category=category)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    db.close()
    return new_category
