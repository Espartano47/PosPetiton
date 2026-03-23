from pydantic import BaseModel
from typing import List, Optional


class PurchaseItem(BaseModel):
    product_id: int
    quantity: float
    cost: float


class PurchaseCreate(BaseModel):
    supplier_id: int
    user_id: Optional[int]
    invoice_number: Optional[str]
    status: str
    items: List[PurchaseItem]


class Purchase(BaseModel):
    id: int
    supplier_id: int
    user_id: Optional[int]
    invoice_number: Optional[str]
    status: str
    total: float

    class Config:
        orm_mode = True