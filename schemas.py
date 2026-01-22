from pydantic import BaseModel
from typing import Optional

class Empleado(BaseModel):
    nombre: str
    departamento: str
    puesto: str
    salario: float
    fecha_ingreso: Optional[str] = None
    estado: Optional[str] = "Activo"