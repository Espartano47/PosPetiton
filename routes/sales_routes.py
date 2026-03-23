from fastapi import APIRouter, Depends,Query
from models.sales import SaleCreate
from funtions.sales import crear_venta, listar_ventas_paginadas

from config.database import get_db
from funtions.auth import get_current_user


router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"]
)



@router.post("/")
def crear_venta_endpoint(
    venta: SaleCreate,
    db=Depends(get_db),
    user=Depends(get_current_user)
):

    sale_id = crear_venta(db, venta, user["id"])

    return {
        "message": "Venta registrada",
        "sale_id": sale_id
    }


@router.get("/historial")
def historial_ventas(
    db=Depends(get_db),
    user=Depends(get_current_user),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    search: str = Query('', max_length=50)
):
    """
    Retorna ventas con paginación y búsqueda por nombre de cliente o producto.
    """
    return listar_ventas_paginadas(db, page, limit, search)