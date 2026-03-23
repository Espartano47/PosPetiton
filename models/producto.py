from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductoBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    cost: Optional[float] = None
    stock: int = 0
    min_stock: int = 0
    barcode: Optional[str] = None
    status: int = 1
    image: Optional[str] = None  # <-- nueva propiedad

class ProductoCreate(ProductoBase):
    created_by: Optional[int] = None  # se asigna automáticamente desde el backend

class ProductoUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    cost: Optional[float] = None
    stock: Optional[int] = None
    min_stock: Optional[int] = None
    barcode: Optional[str] = None
    status: Optional[int] = None
    image: Optional[str] = None  # <-- también opcional para editar
    updated_by: Optional[int] = None

class ProductoOut(ProductoBase):
    id: int
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True