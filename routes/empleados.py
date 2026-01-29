from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from config.database import get_db
from typing import Optional
from funtions.guardarfoto import guardar_foto
from models.empleado import Empleado
from funtions.empleados import (
    obtener_empleados,
    obtener_empleado_por_id,
    insertar_empleado,
    actualizar_empleado,
    eliminar_empleado
)
from config.dependencies import has_permission
from funtions.auth import get_current_user  

router = APIRouter(prefix="/empleados", tags=["Empleados"])

#Todos los empleados
@router.get("/", response_model=list[Empleado])
def listar_empleados(
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("empleados:read"))
    ):
    return obtener_empleados(db)

#crear empleados
@router.post("/", response_model=Empleado)
def crear_empleado(
    nombre: str = Form(...),
    departamento: str = Form(...),
    puesto: str = Form(...),
    salario: float = Form(...),
    fecha_ingreso: str = Form(...),
    estado: str = Form(...),
    foto: Optional[UploadFile] = File(None),
    db = Depends(get_db),
    current_user = Depends(get_current_user),
    permiso_valido=Depends(has_permission("empleados:create"))
):
    # Guardar foto si existe
    foto_path = None
    if foto:
        foto_path = guardar_foto(foto)

    # Crear diccionario para insertar en DB
    empleado_data = {
        "nombre": nombre,
        "departamento": departamento,
        "puesto": puesto,
        "salario": salario,
        "fecha_ingreso": fecha_ingreso,
        "estado": estado,
        "foto": foto_path
    }
    print(current_user)
    # Insertar en DB pasando también quien crea el registro
    empleado_id = insertar_empleado(
        db, 
        empleado_data,
        usuario_id=current_user["id"],
        usuario_nombre=current_user["username"],
        empresaId=current_user["empresaId"]
    )

    empleado_completo = obtener_empleado_por_id(db, empleado_id)

    return empleado_completo

@router.get("/{empleado_id}", response_model=Empleado)
def obtener_empleado(
    empleado_id: int,
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("empleados:read"))   
):
    empleado = obtener_empleado_por_id(db, empleado_id)

    if not empleado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empleado no encontrado"
        )

    return empleado

@router.delete("/{empleado_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_empleado_endpoint(
    empleado_id: int,
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("empleados:delete"))
):
    eliminado = eliminar_empleado(db, empleado_id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empleado no encontrado"
        )
    

@router.put("/{empleado_id}", response_model=Empleado)
def actualizar_empleado_endpoint(
    empleado_id: int,
    empleado: Empleado,
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("empleados:update"))
):
    actualizado = actualizar_empleado(db, empleado_id, empleado)

    if not actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empleado no encontrado"
        )

    empleado.id = empleado_id
    return empleado