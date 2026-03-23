from pydantic import BaseModel
from typing import List, Optional


class SaleItem(BaseModel):
    id: int
    name: str
    price: float
    cantidad: int


class SaleCreate(BaseModel):

    items: List[SaleItem]

    total: float

    tipo: str

    cliente_id: Optional[int] = None