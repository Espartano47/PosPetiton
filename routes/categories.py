from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.categories import Category, CategoryCreate, CategoryUpdate
from config.database import get_db
from funtions.categories import (
    crear_category,
    obtener_categories,
    obtener_category,
    actualizar_category,
    eliminar_category
)

router = APIRouter(prefix="/categories", tags=["Categories"])

# ---------------- GET ALL ----------------
@router.get("/", response_model=List[Category])
def list_categories(db=Depends(get_db)):
    return obtener_categories(db)

# ---------------- GET ONE ----------------
@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int, db=Depends(get_db)):
    category = obtener_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

# ---------------- CREATE ----------------
@router.post("/", response_model=Category)
def create_category(category: CategoryCreate, db=Depends(get_db)):
    crear_category(db, category.dict())
    return obtener_categories(db)[0]

# ---------------- UPDATE ----------------
@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryUpdate, db=Depends(get_db)):
    existing = obtener_category(db, category_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Category not found")
    actualizar_category(db, category_id, category.dict())
    return obtener_category(db, category_id)

# ---------------- DELETE ----------------
@router.delete("/{category_id}")
def delete_category(category_id: int, db=Depends(get_db)):
    existing = obtener_category(db, category_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Category not found")
    eliminar_category(db, category_id)
    return {"message": "Category deleted successfully"}