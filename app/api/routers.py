from fastapi import APIRouter, Depends
from app.db.models.categories import Categories
from app.db.database import get_db
from app.middleware.exceptions import NotFoundException

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "OK"}

@router.get("/categories/{id}")
def get_category_by_id(id: str, db=Depends(get_db)):
    category = db.query(Categories).filter(Categories.id == id).first()
    if not category:
        raise NotFoundException(detail=f"Category with id {id} not found.")
    return {"id": category.id, "category": category.category}
