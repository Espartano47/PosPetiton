from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from funtions.role import crear_rol, editar_rol, obtener_roles, eliminar_rol
from models.role import RoleCreate, RoleUpdate

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/")
def list_roles(db=Depends(get_db)):
    return {"data": obtener_roles(db)}

@router.post("/")
def create_role_endpoint(role: RoleCreate, db=Depends(get_db)):
    role_dict = role.model_dump()
    crear_rol(db, role_dict)
    return {"message": "Rol creado correctamente"}

@router.put("/{role_id}")
def update_role_endpoint(role_id: int, role: RoleUpdate, db=Depends(get_db)):
    editar_rol(db, role_id, role.model_dump())
    return {"message": "Rol actualizado correctamente"}

@router.delete("/{role_id}")
def delete_role_endpoint(role_id: int, db=Depends(get_db)):
    eliminar_rol(db, role_id)
    return {"message": "Rol eliminado correctamente"}