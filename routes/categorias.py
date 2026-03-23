from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from config.database import get_db
from typing import Optional
from funtions.guardarfoto import guardar_foto
from models.categorias import categoria
from funtions.categorias import (
    obtener_categorias,
    obtener_categorias_byname
)
from config.dependencies import has_permission
from funtions.auth import get_current_user  

router = APIRouter(prefix="/categorias", tags=["categorias"])

#Todas las categorias
@router.get("/", response_model=list[categoria])
def listar_categorias(
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("empleados:read"))
    ):
    return obtener_categorias(db)

#Todas las categorias
@router.get("/{categoriaName}", response_model=list[categoria])
def listar_categorias(
    categoriaName = str,
    user=Depends(get_current_user),
    db=Depends(get_db),
    permiso_valido=Depends(has_permission("empleados:read"))
    ):
    return obtener_categorias_byname(db,categoriaName)
