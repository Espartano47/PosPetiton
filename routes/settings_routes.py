import os
from fastapi import APIRouter, Depends, UploadFile, File, Form
from funtions.settings import actualizar_configuracion, obtener_configuracion, crear_configuracion
from config.database import get_db
from fastapi import HTTPException, Request


router = APIRouter(prefix="/settings", tags=["Configuraciones"])

# ---------------- OBTENER CONFIG ----------------
@router.get("/")
def get_settings(request: Request, db=Depends(get_db)):
    config = obtener_configuracion(db)
    if config.get("logo"):
        # Construye URL absoluta
        config["logo"] = str(request.base_url)[:-1] + config["logo"]
    return config

# ---------------- ACTUALIZAR CONFIG ----------------
@router.put("/")
def update_settings(
    system_name: str = Form(...),
    currency: str = Form(...),
    tax: float = Form(0),
    business_name: str = Form(None),
    phone: str = Form(None),
    email: str = Form(None),
    address: str = Form(None),
    logo: UploadFile | None = File(None),
    db=Depends(get_db)
):
    # obtener el id de la fila existente
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id FROM settings LIMIT 1")
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="No se encontró configuración")
    config_id = row["id"]

    data = {
        "id": config_id,  # <--- ahora sí existe
        "system_name": system_name,
        "currency": currency,
        "tax": tax,
        "business_name": business_name,
        "phone": phone,
        "email": email,
        "address": address,
    }

    if logo:
        folder = "static/logos"
        os.makedirs(folder, exist_ok=True)
        file_location = os.path.join(folder, logo.filename)
        with open(file_location, "wb") as f:
            f.write(logo.file.read())
        data["logo"] = f"/static/logos/{logo.filename}" 

    actualizar_configuracion(db, data)
    return {"message": "Configuración actualizada"}

# ---------------- CREAR CONFIG (solo para inicializar) ----------------
@router.post("/")
def create_settings(
    system_name: str = Form(...),
    currency: str = Form(...),
    tax: float = Form(0),
    business_name: str = Form(None),
    phone: str = Form(None),
    email: str = Form(None),
    address: str = Form(None),
    logo: UploadFile | None = File(None),
    db=Depends(get_db)
):
    data = {
        "system_name": system_name,
        "currency": currency,
        "tax": tax,
        "business_name": business_name,
        "phone": phone,
        "email": email,
        "address": address,
        "logo": None
    }

    if logo:
        file_location = f"static/logos/{logo.filename}"
        with open(file_location, "wb") as f:
            f.write(logo.file.read())
        data["logo"] = file_location

    crear_configuracion(db, data)
    return {"message": "Configuración creada"}