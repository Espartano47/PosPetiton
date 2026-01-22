from fastapi import APIRouter

router = APIRouter(prefix="/vacaciones", tags=["Vacaciones"])

@router.get("/")
def get_vacaciones():
    return {"mensaje": "Módulo de vacaciones pendiente"}