from pydantic import BaseModel
from typing import List, Optional

class QuotationItem(BaseModel):
    id: int
    name: str
    price: float
    cantidad: int


class QuotationBase(BaseModel):
    client_id: Optional[int] = None
    total: float


class QuotationCreate(QuotationBase):
    items: List[QuotationItem]


class QuotationUpdate(QuotationBase):
    pass


class Quotation(QuotationBase):
    id: int

    class Config:
        orm_mode = True