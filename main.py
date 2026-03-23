from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes.usuarios import router as usuarios_router
from routes.configuraciones import router as configuraciones
from routes.categorias import router as categorias
from routes.producto import router as productos_router
from routes.customer import router as customer_router
from routes.settings_routes import router as settings_router
from routes.sales_routes import router as sales_router
from routes.roles import router as roles_router
from routes.permissions import router as permissions_router
import os
from fastapi.staticfiles import StaticFiles
from routes.suppliers import router as suppliers_router
from routes.categories import router as categories_router
from routes.inventory_movements import router as inventory_movements_router
from routes.purchases import router as purchases_router
from routes.quotation_router import router as quotation_router


app = FastAPI(title="API RRHH con FastAPI")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


os.makedirs("static/logos", exist_ok=True)  # asegúrate que exista la carpeta

app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React por defecto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(usuarios_router)
app.include_router(configuraciones)
app.include_router(categorias)
app.include_router(productos_router)
app.include_router(customer_router)
app.include_router(settings_router)
app.include_router(sales_router)
app.include_router(roles_router)
app.include_router(permissions_router)
app.include_router(suppliers_router)
app.include_router(categories_router)
app.include_router(inventory_movements_router)
app.include_router(purchases_router)
app.include_router(quotation_router)