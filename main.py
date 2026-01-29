from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from routes.empleados import router as empleados_router
from routes.asistencia import router as asistencia_router
from routes.vacaciones import router as vacaciones_router
from routes.auth import router as auth_router
from routes.usuarios import router as usuarios_router

app = FastAPI(title="API RRHH con FastAPI")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# ✅ IMPORTANTE: Permitir que React se conecte a FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # React (Vite)
        "http://127.0.0.1:5173","http://localhost:8080","http://127.0.0.1:8080"
    ],  # React por defecto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(empleados_router)
app.include_router(asistencia_router)
app.include_router(vacaciones_router)
app.include_router(auth_router)
app.include_router(usuarios_router)

# @app.get("/")
# def root():
#     return {"mensaje": "API RRHH funcionando con FastAPI 🚀"}
