from config.database import get_connection
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from config.security import SECRET_KEY, ALGORITHM,verify_password, hash_password
from datetime import datetime,timezone

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_user_by_username(username: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM usuarios_con_empresaa WHERE username = %s",
        (username,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()
    return user


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

    user = get_user_by_username(username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )
    return user


def cambiar_password_usuario(
    db,
    user_id: int,
    current_password: str,
    new_password: str
):
    cursor = db.cursor(dictionary=True)

    # Obtener usuario
    cursor.execute(
        "SELECT id, password FROM rrhh.usuarios WHERE id = %s",
        (user_id,)
    )
    user = cursor.fetchone()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    # Verificar contraseña actual
    if not verify_password(current_password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña actual es incorrecta"
        )

    # Evitar reutilizar contraseña
    if verify_password(new_password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La nueva contraseña no puede ser igual a la anterior"
        )

    # Hashear nueva contraseña
    new_hashed_password = hash_password(new_password)

    # Actualizar contraseña y flags
    cursor.execute(
        """
        UPDATE rrhh.usuarios
        SET password = %s,
            forcePasswordChange = FALSE,
            LastLogin = %s
        WHERE id = %s
        """,
        (
            new_hashed_password,
            datetime.now(timezone.utc),
            user_id
        )
    )
    db.commit()
    return True