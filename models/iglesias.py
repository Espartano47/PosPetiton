from pydantic import BaseModel
from datetime import date,datetime
from typing import Optional

class iglesia(BaseModel):
    id: Optional[int] = None
    fecha_fundacion: Optional[date]
    nombre: Optional[str]
    direccion: Optional[str]
    sector: Optional[str]
    ciudad: Optional[str]
    provincia: Optional[str]
    municipio: Optional[str]
    telefono: Optional[str]
    imagen: Optional[str]