import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "uploads/empleados"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def guardar_foto(file: UploadFile) -> str:

    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as f:
        f.write(file.file.read())


    url = f"/{path.replace(os.sep, '/')}"
    return url


UPLOAD_DIR2 = "uploads/usuarios"
os.makedirs(UPLOAD_DIR2, exist_ok=True)
def guardar_foto_usuario(file: UploadFile) -> str:

    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    path = os.path.join(UPLOAD_DIR2, filename)

    with open(path, "wb") as f:
        f.write(file.file.read())

    url = f"/{path.replace(os.sep, '/')}"
    return url