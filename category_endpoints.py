from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db
from app.schemas.category import Category, CategoryCreate, CategoryUpdate
from app.services.category_service import CategoryService

router = APIRouter()

@router.post("/categories/", response_model=Category)
def create_category(category_create: CategoryCreate, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    return category_service.create_category(category_create)

@router.get("/categories/", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    return category_service.get_all_categories(skip, limit)

@router.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    category = category_service.get_category(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
