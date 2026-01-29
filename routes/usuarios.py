from fastapi import APIRouter, HTTPException, Depends, status, UploadFile, File, Form
from pydantic import BaseModel
from funtions.usuarios import crear_usuario,obtener_usuarios,obtener_usuario_por_id,editar_usuario,eliminar_usuario
from config.security import hash_password
from mysql.connector.errors import IntegrityError
from funtions.auth import get_current_user 
from config.database import get_db
from models.usuario import UsuarioOut,UsuarioCreate
from config.dependencies import has_permission
from typing import Optional
from funtions.guardarfoto import guardar_foto_usuario

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

#obtener por ID
@router.get("/{usuario_id}", response_model=UsuarioOut)
def obtener_usuario(
    usuario_id: int,
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("usuarios:read"))
):
    empleado = obtener_usuario_por_id(db, usuario_id)

    if not empleado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empleado no encontrado"
        )
    return empleado


#Todos los usuarios
@router.get("/", response_model=list[UsuarioOut])
def listarusuarios(
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("usuarios:read"))
    ):
    return obtener_usuarios(db)

@router.post("/")
def crear_usuario_endpoint(
    user=Depends(get_current_user),
    username: str = Form(...),
    password: str = Form(...),
    rol: str = Form(...),
    Nombre: str = Form(...),
    Correo: str = Form(...),
    foto: Optional[UploadFile] = File(None),
    db = Depends(get_db),
    permiso_valido=Depends(has_permission("usuarios:create"))):

    try:
        password_hash = hash_password(password)

        # Guardar foto si existe
        foto_path = None
        if foto:
            foto_path = guardar_foto_usuario(foto)

        # Crear diccionario para insertar en DB
        usuario_data = {
            "nombre": Nombre,
            "username":username,
            "password": password_hash,
            "rol": rol,
            "Correo": Correo,
            "foto":foto_path
        }

        crear_usuario(
            db,
            usuario_data,
            usuario_id=user["id"],
            usuario_nombre=user["username"],
            empresaId=user["empresaId"]
        )

        return {"message": "Usuario creado correctamente"}
    
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="El usuario ya existe"
        )

@router.put("/{usuario_id}")
def editar_usuario_endpoint(
    usuario_id: int,
    user=Depends(get_current_user),

    # CAMPOS EDITABLES
    Nombre: str = Form(...),
    Correo: str = Form(...),
    rol: str = Form(...),
    username: str = Form(...),
    foto: Optional[UploadFile] = File(None),

    db = Depends(get_db),
    permiso_valido=Depends(has_permission("usuarios:update"))
):
    try:
        datos_actualizar = {
            "nombre": Nombre,
            "Correo": Correo,
            "role": rol,
            "username": username
        }

        # 🖼️ Si envía nueva foto, se reemplaza
        if foto:
            foto_path = guardar_foto_usuario(foto)
            datos_actualizar["foto"] = foto_path

        editar_usuario(
            db,
            usuario_id,
            datos_actualizar
        )

        return {"message": "Usuario actualizado correctamente"}

    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="El username o correo ya existe"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.delete("/{usuario_id}")
def eliminar_usuario_endpoint(
    usuario_id: int,
    user=Depends(get_current_user),
    db = Depends(get_db),
    permiso_valido=Depends(has_permission("usuarios:delete"))
    ):
    try:
        eliminar_usuario( db,
                usuario_id)
        
        return {"message": "Usuario actualizado correctamente"}
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )