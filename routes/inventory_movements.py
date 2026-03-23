from fastapi import APIRouter, Depends, HTTPException
from typing import List

from models.inventory_movements import (
    InventoryMovement,
    InventoryMovementCreate,
    InventoryMovementUpdate
)

from config.database import get_db

from funtions.inventory_movements import (
    crear_movimiento,
    obtener_movimientos,
    obtener_movimiento,
    actualizar_movimiento,
    eliminar_movimiento
)

router = APIRouter(
    prefix="/inventory-movements",
    tags=["Inventory Movements"]
)


# ---------------- GET ALL ----------------
@router.get("/", response_model=List[InventoryMovement])
def list_movements(db=Depends(get_db)):
    return obtener_movimientos(db)


# ---------------- GET ONE ----------------
@router.get("/{movement_id}", response_model=InventoryMovement)
def get_movement(movement_id: int, db=Depends(get_db)):

    movement = obtener_movimiento(db, movement_id)

    if not movement:
        raise HTTPException(status_code=404, detail="Movement not found")

    return movement


# ---------------- CREATE ----------------
@router.post("/", response_model=InventoryMovement)
def create_movement(data: InventoryMovementCreate, db=Depends(get_db)):

    crear_movimiento(db, data.dict())

    return obtener_movimientos(db)[0]


# ---------------- UPDATE ----------------
@router.put("/{movement_id}", response_model=InventoryMovement)
def update_movement(movement_id: int, data: InventoryMovementUpdate, db=Depends(get_db)):

    existing = obtener_movimiento(db, movement_id)

    if not existing:
        raise HTTPException(status_code=404, detail="Movement not found")

    actualizar_movimiento(db, movement_id, data.dict())

    return obtener_movimiento(db, movement_id)


# ---------------- DELETE ----------------
@router.delete("/{movement_id}")
def delete_movement(movement_id: int, db=Depends(get_db)):

    existing = obtener_movimiento(db, movement_id)

    if not existing:
        raise HTTPException(status_code=404, detail="Movement not found")

    eliminar_movimiento(db, movement_id)

    return {"message": "Movement deleted successfully"}