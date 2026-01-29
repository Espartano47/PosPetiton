from fastapi import APIRouter, HTTPException, Depends
from funtions.auth import get_current_user 
from config.database import get_db
from funtions.configuraciones import obtener_permisos,obtener_permisosbyuser,agregar_permisosbyuser,eliminar_permisosbyuser
from pydantic import BaseModel

router = APIRouter(
    prefix="/configuraciones",
    tags=["configuraciones"]
)

class PermisoUsuarioCreate(BaseModel):
    usuario_id: int
    permiso_id: int

obtener_permisosbyuser
#Todos los permisos
@router.get("/permisos")
def listapermisos(
    user=Depends(get_current_user),
    db=Depends(get_db)
    ):
    return obtener_permisos(db)

#Todos los permisos del usuario
@router.get("/permisos/{usuario_id}")
def listapermisosuser(
    usuario_id: int,
    user=Depends(get_current_user),
    db=Depends(get_db)
    ):
    return obtener_permisosbyuser(db,usuario_id)

#Todos los permisos del usuario
@router.get("/permisos/{usuario_id}")
def listapermisosuser(
    usuario_id: int,
    user=Depends(get_current_user),
    db=Depends(get_db)
    ):
    return obtener_permisosbyuser(db,usuario_id)


@router.post("/permisos/asignar")
def asignar_permiso_usuario(
    data: PermisoUsuarioCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
    ):
    return agregar_permisosbyuser(db,data.usuario_id,data.permiso_id)
    


@router.delete("/permisos/quitar")
def quitar_permiso_usuario(
    data: PermisoUsuarioCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
    ):
    return eliminar_permisosbyuser(db,data.usuario_id,data.permiso_id)
