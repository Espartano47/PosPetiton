from fastapi import APIRouter, Depends
from config.database import get_db
from models.empleado import Empleado
from funtions.empleados import obtener_empleados, insertar_empleado
from config.dependencies import get_current_user

router = APIRouter(prefix="/empleados", tags=["Empleados"])

# @router.get("/", response_model=list[Empleado])
# def get_empleados(db=Depends(get_db)):
#     return obtener_empleados(db)

@router.get("/")
def listar_empleados(user=Depends(get_current_user)):
    return {
        "message": "Acceso autorizado",
        "usuario": user
    }

@router.post("/", response_model=Empleado)
def crear_empleado(empleado: Empleado, db=Depends(get_db)):
    empleado.id = insertar_empleado(db, empleado)
    return empleado
