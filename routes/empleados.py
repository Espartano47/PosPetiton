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
@router.get("/")
def listar_empleados(
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("empleados:read"))
    ):
    return obtener_empleados(db)

#crear empleados
@router.post("/", response_model=Empleado)
def crear_empleado(
    identificacion: Optional[str] = Form(None),
    nombre: Optional[str] = Form(None),
    apellido: Optional[str] = Form(None),
    genero: Optional[str] = Form(None),
    nacimiento: Optional[str] = Form(None),
    tipoSangre: Optional[str] = Form(None),
    estadoCivil: Optional[str] = Form(None),
    bautizado: Optional[str] = Form(None),
    telefono: Optional[str] = Form(None),
    celular: Optional[str] = Form(None),
    correo: Optional[str] = Form(None),
    Ocupacion: Optional[str] = Form(None),
    provincia: Optional[str] = Form(None),
    municipio: Optional[str] = Form(None),
    sector: Optional[str] = Form(None),
    direccion: Optional[str] = Form(None),
    iglesia_id: Optional[int]= Form(None),
    id_categoria: Optional[int]= Form(None),
    foto:Optional[UploadFile] = File(None),
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
        "identificacion": identificacion,
        "nombre": nombre,
        "apellido": apellido,
        "genero": genero,
        "nacimiento": nacimiento,
        "tipoSangre": tipoSangre,
        "estadoCivil": estadoCivil,
        "bautizado": bautizado,
        "telefono": telefono,
        "celular": celular,
        "correo": correo,
        "Ocupacion": Ocupacion,
        "provincia": provincia,
        "municipio": municipio,
        "sector": sector,
        "direccion": direccion,
        "iglesia_id":iglesia_id,
        "id_categoria":id_categoria,
        "foto": foto_path
    }
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

@router.get("/{empleado_id}")
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
    

@router.put("/{empleado_id}")
def actualizar_empleado_endpoint(
    empleado_id: int,
    identificacion: Optional[str] = Form(None),
    nombre: Optional[str] = Form(None),
    apellido: Optional[str] = Form(None),
    genero: Optional[str] = Form(None),
    nacimiento: Optional[str] = Form(None),
    tipoSangre: Optional[str] = Form(None),
    estadoCivil: Optional[str] = Form(None),
    bautizado: Optional[str] = Form(None),
    telefono: Optional[str] = Form(None),
    celular: Optional[str] = Form(None),
    correo: Optional[str] = Form(None),
    Ocupacion: Optional[str] = Form(None),
    provincia: Optional[str] = Form(None),
    municipio: Optional[str] = Form(None),
    sector: Optional[str] = Form(None),
    direccion: Optional[str] = Form(None),
    id_iglesia: Optional[str] = Form(None),
    id_categoria: Optional[str] = Form(None),
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("empleados:update"))
):  
    if id_iglesia in (None, "", "NaN"):
        id_iglesia = None
    else:
        id_iglesia = int(id_iglesia)

    empleado_data = {
        "identificacion": identificacion,
        "nombre": nombre,
        "apellido": apellido,
        "genero": genero,
        "nacimiento": nacimiento,
        "tipoSangre": tipoSangre,
        "estadoCivil": estadoCivil,
        "bautizado": bautizado,
        "telefono": telefono,
        "celular": celular,
        "correo": correo,
        "Ocupacion": Ocupacion,
        "provincia": provincia,
        "municipio": municipio,
        "sector": sector,
        "direccion": direccion,
        "id_iglesia":id_iglesia,
        "id_categoria":int(id_categoria)
    }

    actualizar_empleado(db, empleado_id, empleado_data)
    return {"message": "Usuario actualizado correctamente"}