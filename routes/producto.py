from fastapi import APIRouter, HTTPException, Depends, status, Form
from typing import Optional
from models.producto import ProductoCreate, ProductoUpdate, ProductoOut
from funtions.guardarfoto import guardar_foto_producto
from funtions.producto import (
    crear_producto,
    obtener_productos,
    obtener_producto_por_id,
    obtener_producto_por_nombre,
    editar_producto,
    eliminar_producto
)
from config.database import get_db
from funtions.auth import get_current_user
from config.dependencies import has_permission
from models.producto import ProductoOut
from fastapi import UploadFile, File, Form

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

# ---------------- GET PRODUCTO POR ID ----------------
@router.get("/{producto_id}", response_model=ProductoOut)
def obtener_producto_endpoint(
    producto_id: int,
    user=Depends(get_current_user),
    db=Depends(get_db),
    # permiso_valido=Depends(has_permission("productos:read"))
):
    producto = obtener_producto_por_id(db, producto_id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    return producto

# ---------------- GET PRODUCTO POR NOMBRE ----------------
@router.get("/nombre/{nombre}", response_model=ProductoOut)
def obtener_producto_nombre_endpoint(
    nombre: str,
    user=Depends(get_current_user),
    db=Depends(get_db),
    # permiso_valido=Depends(has_permission("productos:read"))
):
    producto = obtener_producto_por_nombre(db, nombre)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    return producto

# ---------------- LISTAR TODOS LOS PRODUCTOS ----------------
@router.get("/", response_model=list[ProductoOut])
def listar_productos(
    user=Depends(get_current_user),
    db=Depends(get_db),
    # permiso_valido=Depends(has_permission("productos:read"))
):
    return obtener_productos(db)

# ---------------- CREAR PRODUCTO ----------------
@router.post("/")
def crear_producto_endpoint(
    producto: ProductoCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):

    producto_dict = producto.model_dump()

    crear_producto(db, producto_dict, usuario_id=user["id"])

    return {"message": "Producto creado correctamente"}

# ---------------- ACTUALIZAR PRODUCTO ----------------
@router.put("/{producto_id}")
def editar_producto_endpoint(
    producto_id: int,
    name: str = Form(None),
    description: str = Form(None),
    price: float = Form(None),
    cost: float = Form(None),
    stock: int = Form(None),
    image: UploadFile = File(None),
    user=Depends(get_current_user),
    db=Depends(get_db),
):
    datos_actualizar = {}
    print(f"DEBUG: name={name}, price={price}")

    if name is not None: datos_actualizar["name"] = name
    if description is not None: datos_actualizar["description"] = description
    if price is not None: datos_actualizar["price"] = price
    if cost is not None: datos_actualizar["cost"] = cost
    if stock is not None: datos_actualizar["stock"] = stock
    if image is not None: datos_actualizar["image"] = guardar_foto_producto(image)

    if not datos_actualizar:
        raise HTTPException(status_code=400, detail="No hay campos para actualizar")

    editar_producto(db, producto_id, datos_actualizar, usuario_id=user["id"])

    return {"message": "Producto actualizado correctamente"}


# ---------------- ELIMINAR PRODUCTO ----------------
@router.delete("/{producto_id}")
def eliminar_producto_endpoint(
    producto_id: int,
    user=Depends(get_current_user),
    db=Depends(get_db),
    # permiso_valido=Depends(has_permission("productos:delete"))
):
    eliminar_producto(db, producto_id)
    return {"message": "Producto eliminado correctamente"}