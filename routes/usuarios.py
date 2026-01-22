from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from funtions.usuarios import crear_usuario
from config.security import hash_password
from mysql.connector.errors import IntegrityError

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

class UsuarioCreate(BaseModel):
    username: str
    password: str
    rol: str = "user"

@router.post("/")
def crear_usuario_endpoint(data: UsuarioCreate):
    try:
        password_hash = hash_password(data.password)

        crear_usuario(
            username=data.username,
            password=password_hash,
            rol=data.rol
        )

        return {"message": "Usuario creado correctamente"}

    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="El usuario ya existe"
        )
