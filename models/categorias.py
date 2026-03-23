from pydantic import BaseModel
from typing import Optional

class categoria(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str]
    descripcion: Optional[str]