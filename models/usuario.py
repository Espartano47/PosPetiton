from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UsuarioLogin(BaseModel):
    username: str
    password: str

class UsuarioOut(BaseModel):
    id:int
    Nombre: str | None = None
    Correo: str | None = None
    username: str
    role: str
    estado: str
    foto: str | None = None
    created: datetime
    LastLogin: datetime | None = None
    createByName: str | None = None
    createById: int | None = None
    empresaId: int | None = None
    NombreEmpresa: str | None = None
    Pais: str | None = None
    forcePasswordChange:int
    permisos: str | None = None

class UsuarioCreate(BaseModel):
    username: str
    password: str
    rol: str = "user"
    Nombre: str | None = None
    Correo: str | None = None
    foto: Optional[str]
    forcePasswordChange:int
    
class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str
