from fastapi import APIRouter, Depends
from typing import List

from models.purchases import Purchase, PurchaseCreate
from config.database import get_db
from funtions.purchases import crear_compra, obtener_compras

router = APIRouter(prefix="/purchases", tags=["Purchases"])


# ---------------- GET ALL ----------------
@router.get("/", response_model=List[Purchase])
def list_purchases(db=Depends(get_db)):
    return obtener_compras(db)


# ---------------- CREATE ----------------
@router.post("/", response_model=Purchase)
def create_purchase(data: PurchaseCreate, db=Depends(get_db)):

    purchase_id = crear_compra(db, data.dict())

    compras = obtener_compras(db)

    for c in compras:
        if c["id"] == purchase_id:
            return c