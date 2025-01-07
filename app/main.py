from fastapi import FastAPI
from .database import Base, engine
from .routes import citas
from .middleware import add_cors_middleware

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Salón de Belleza")

# Configurar CORS
add_cors_middleware(app)

# Incluir rutas
app.include_router(citas.router, prefix="/citas", tags=["Citas"])
