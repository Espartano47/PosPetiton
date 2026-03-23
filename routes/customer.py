from fastapi import APIRouter, Depends
from config.database import get_db
from funtions.customer import *
from models.customer import CustomerCreate, CustomerUpdate
from funtions.auth import get_current_user

router = APIRouter(prefix="/clientes", tags=["Clientes"])


# ---------------- LISTAR CLIENTES ----------------
@router.get("/")
def listar_clientes(db=Depends(get_db)):
    return obtener_clientes(db)


# ---------------- OBTENER CLIENTE ----------------
@router.get("/{cliente_id}")
def obtener_cliente_endpoint(cliente_id: int, db=Depends(get_db)):
    return obtener_cliente(db, cliente_id)


# ---------------- CREAR CLIENTE ----------------
@router.post("/")
def crear_cliente_endpoint(
    cliente: CustomerCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):

    crear_cliente(
        db,
        cliente.dict(),
        usuario_id=user["id"]
    )

    return {"message": "Cliente creado correctamente"}


# ---------------- ACTUALIZAR CLIENTE ----------------
@router.put("/{cliente_id}")
def actualizar_cliente_endpoint(
    cliente_id: int,
    cliente: CustomerUpdate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):

    actualizar_cliente(
        db,
        cliente_id,
        cliente.dict(),
        usuario_id=user["id"]
    )

    return {"message": "Cliente actualizado correctamente"}


# ---------------- ELIMINAR CLIENTE ----------------
@router.delete("/{cliente_id}")
def eliminar_cliente_endpoint(cliente_id: int, db=Depends(get_db)):

    eliminar_cliente(db, cliente_id)

    return {"message": "Cliente eliminado"}