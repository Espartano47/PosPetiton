from fastapi import APIRouter, Depends, HTTPException
from typing import List
from config.database import get_db

from models.quotations import (
    Quotation,
    QuotationCreate,
    QuotationUpdate
)

from funtions.quotations import (
    crear_quotation,
    obtener_quotations,
    obtener_quotation,
    actualizar_quotation,
    eliminar_quotation
)

router = APIRouter(
    prefix="/quotations",
    tags=["Quotations"]
)


# ---------- GET ALL ----------

@router.get("/", response_model=List[Quotation])
def list_quotations(db=Depends(get_db)):
    return obtener_quotations(db)


# ---------- GET ONE ----------

@router.get("/{quotation_id}", response_model=Quotation)
def get_quotation(quotation_id: int, db=Depends(get_db)):

    quotation = obtener_quotation(db, quotation_id)

    if not quotation:
        raise HTTPException(status_code=404, detail="Quotation not found")

    return quotation


# ---------- CREATE ----------

@router.post("/", response_model=Quotation)
def create_quotation(data: QuotationCreate, db=Depends(get_db)):

    quotation_id = crear_quotation(db, data.dict())

    return obtener_quotation(db, quotation_id)


# ---------- UPDATE ----------

@router.put("/{quotation_id}", response_model=Quotation)
def update_quotation(
    quotation_id: int,
    quotation: QuotationUpdate,
    db=Depends(get_db)
):

    existing = obtener_quotation(db, quotation_id)

    if not existing:
        raise HTTPException(status_code=404, detail="Quotation not found")

    actualizar_quotation(db, quotation_id, quotation.dict())

    return obtener_quotation(db, quotation_id)


# ---------- DELETE ----------

@router.delete("/{quotation_id}")
def delete_quotation(quotation_id: int, db=Depends(get_db)):

    existing = obtener_quotation(db, quotation_id)

    if not existing:
        raise HTTPException(status_code=404, detail="Quotation not found")

    eliminar_quotation(db, quotation_id)

    return {"message": "Quotation deleted successfully"}