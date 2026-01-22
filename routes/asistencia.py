from fastapi import APIRouter

router = APIRouter(prefix="/asistencia", tags=["Asistencia"])

@router.get("/")
def get_asistencia():
    return {"mensaje": "Módulo de asistencia pendiente"}