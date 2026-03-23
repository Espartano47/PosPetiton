from fastapi import APIRouter, Depends
from config.database import get_db

router = APIRouter(prefix="/permissions", tags=["Permissions"])

@router.get("/")
def list_permissions(db=Depends(get_db)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, name, description FROM permissions")
    permisos = cursor.fetchall()
    cursor.close()
    db.close()
    return {"data": permisos}