from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InventoryMovementBase(BaseModel):
    product_id: int
    user_id: Optional[int] = None
    type: str
    quantity: float
    stock_before: float
    stock_after: float
    reference: Optional[str] = None


class InventoryMovementCreate(InventoryMovementBase):
    pass


class InventoryMovementUpdate(BaseModel):
    product_id: Optional[int] = None
    user_id: Optional[int] = None
    type: Optional[str] = None
    quantity: Optional[float] = None
    stock_before: Optional[float] = None
    stock_after: Optional[float] = None
    reference: Optional[str] = None


class InventoryMovement(InventoryMovementBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True