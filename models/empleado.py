from pydantic import BaseModel
from datetime import date,datetime
from typing import Optional

class Empleado(BaseModel):
    id: Optional[int] = None

    identificacion: Optional[str]
    nombre: str
    apellido: Optional[str]

    telefono: Optional[str]
    celular: Optional[str]
    correo: Optional[str]

    Ocupacion: Optional[str]
    bautizado: Optional[str]

    nacimiento: Optional[date]

    created: Optional[datetime]
    createdByName: Optional[str]
    createdById: Optional[int]

    empresaId: Optional[int]

    tipoSangre: Optional[str]
    nacionalidad: Optional[str]
    direccion: Optional[str]
    provincia: Optional[str]

    estado: Optional[str]
    genero: Optional[str]
    estadoCivil: Optional[str]
    id_categoria: Optional[int]

    foto: Optional[str]
    id_iglesia: Optional[int]



class Empleadovista(BaseModel):
    id: Optional[int] = None

    identificacion: Optional[str]
    nombre: str
    apellido: Optional[str]

    telefono: Optional[str]
    celular: Optional[str]
    correo: Optional[str]

    Ocupacion: Optional[str]
    bautizado: Optional[str]

    nacimiento: Optional[date]

    created: Optional[datetime]
    createdByName: Optional[str]
    createdById: Optional[int]

    empresaId: Optional[int]

    tipoSangre: Optional[str]
    nacionalidad: Optional[str]
    direccion: Optional[str]
    provincia: Optional[str]

    estado: Optional[str]
    genero: Optional[str]
    estadoCivil: Optional[str]

    foto: Optional[str]
    id_iglesia: Optional[int]
    id_categoria: Optional[int]