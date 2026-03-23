from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.suppliers import Supplier, SupplierCreate, SupplierUpdate
from config.database import get_db
from funtions.suppliers import (
    crear_supplier,
    obtener_suppliers,
    obtener_supplier,
    actualizar_supplier,
    eliminar_supplier
)

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

# ---------------- GET ALL ----------------
@router.get("/", response_model=List[Supplier])
def list_suppliers(db=Depends(get_db)):
    return obtener_suppliers(db)

# ---------------- GET ONE ----------------
@router.get("/{supplier_id}", response_model=Supplier)
def get_supplier(supplier_id: int, db=Depends(get_db)):
    supplier = obtener_supplier(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier

# ---------------- CREATE ----------------
@router.post("/", response_model=Supplier)
def create_supplier(supplier: SupplierCreate, db=Depends(get_db)):
    crear_supplier(db, supplier.dict())
    # Devolver el último insertado
    return obtener_suppliers(db)[0]

# ---------------- UPDATE ----------------
@router.put("/{supplier_id}", response_model=Supplier)
def update_supplier(supplier_id: int, supplier: SupplierUpdate, db=Depends(get_db)):
    existing = obtener_supplier(db, supplier_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Supplier not found")
    actualizar_supplier(db, supplier_id, supplier.dict())
    return obtener_supplier(db, supplier_id)

# ---------------- DELETE ----------------
@router.delete("/{supplier_id}")
def delete_supplier(supplier_id: int, db=Depends(get_db)):
    existing = obtener_supplier(db, supplier_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Supplier not found")
    eliminar_supplier(db, supplier_id)
    return {"message": "Supplier deleted successfully"}