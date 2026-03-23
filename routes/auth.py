from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from funtions.auth import get_user_by_username,get_current_user,cambiar_password_usuario
from config.security import verify_password, create_access_token
from config.database import get_db
from datetime import datetime, timezone
from models.usuario import ChangePasswordRequest

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),db = Depends(get_db)):
    user = get_user_by_username(form_data.username)

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no existe")

    if not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    now_utc = datetime.now(timezone.utc)
    
    cursor = db.cursor()
    cursor.execute(
        """
        UPDATE usuarios
        SET LastLogin = %s
        WHERE id = %s
        """,
        (now_utc, user["id"])
    )
    db.commit()

    token = create_access_token({
        "sub": user["username"],
        "role": user["role"]
    })

    return {
        "access_token": token,
        "UserLogin": user["username"],
        "forcePasswordChange": user["forcePasswordChange"],
        "token_type": "bearer",
        "ImagenProfile": user["foto"]
    }


@router.get("/profile")
def profile(current_user: dict = Depends(get_current_user)):
    return {
        "id": current_user["id"],
        "username": current_user["username"],
        "role": current_user["role"],
        "empresaId": current_user["empresaId"],
        "Nombre": current_user["Nombre"],
        "Correo": current_user["Correo"],
        "foto": current_user["foto"]
    }


@router.post("/change-password")
def change_password(
    data: ChangePasswordRequest,
    current_user: dict = Depends(get_current_user),
    db = Depends(get_db)
):
    cambiar_password_usuario(
        db=db,
        user_id=current_user["id"],
        current_password=data.current_password,
        new_password=data.new_password
    )

    return {
        "message": "Contraseña actualizada correctamente"
    }