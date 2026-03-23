from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from config.database import get_db
from typing import Optional
from funtions.guardarfoto import guardar_foto
from models.iglesias import iglesia
from funtions.iglesias import (
    obtener_iglesias
)
from config.dependencies import has_permission
from funtions.auth import get_current_user  

router = APIRouter(prefix="/iglesias", tags=["iglesias"])

#Todos los iglesias
@router.get("/", response_model=list[iglesia])
def listar_iglesias(
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("empleados:read"))
    ):
    return obtener_iglesias(db)