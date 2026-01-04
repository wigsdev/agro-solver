from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.schemas import DensityInput, PlantingSystem
import os

app = FastAPI(
    title="Agro-Tech Portal",
    description="Portal de servicios agronómicos",
    version="2.0.0"
)

# Configuración CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de Archivos Estáticos y Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- Rutas de Vistas (HTML) ---

@app.get("/")
async def read_home(request: Request):
    """Landing Page"""
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/tools")
async def read_tools(request: Request):
    """Catálogo de Herramientas"""
    return templates.TemplateResponse("tools_hub.html", {"request": request})

@app.get("/tools/density")
async def read_calculator(request: Request):
    """Calculadora de Densidad"""
    return templates.TemplateResponse("calculator.html", {"request": request})

@app.get("/blog")
async def read_blog(request: Request):
    """Blog Page"""
    return templates.TemplateResponse("blog.html", {"request": request})

# --- API Endpoints ---

@app.post("/api/density")
def calculate_density(data: DensityInput):
    """
    Calcula la densidad de siembra basada en las distancias y el sistema.
    """
    try:
        # Fórmula Estándar: 10000 / (d1 * d2)
        base_density = 10000 / (data.row_distance * data.plant_distance)
        
        # Aplicar Factor de Eficiencia para Tresbolillo (Triangular)
        # El factor es 1 / sin(60°) ≈ 1.1547 (lo que significa dividir por 0.866 en el denominador)
        if data.system == PlantingSystem.TRIANGULAR:
            # Fórmula: 10000 / (d1 * d2 * 0.866025)
            plants_per_hectare = base_density / 0.8660254
        else:
            plants_per_hectare = base_density

        return {
            "plants_per_hectare": round(plants_per_hectare),
            "row_distance_used": data.row_distance,
            "plant_distance_used": data.plant_distance,
            "system_used": data.system
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


