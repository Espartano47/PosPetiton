from pydantic import BaseModel
from datetime import date
from typing import Optional

class Empleado(BaseModel):
    id: Optional[int] = None
    nombre: str
    departamento: str
    puesto: str
    salario: float
    fecha_ingreso: date
    estado: str
