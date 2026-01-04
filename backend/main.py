from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.schemas import DensityInput, PlantingSystem
import os

app = FastAPI(
    title="Agro-Solver API",
    description="API Backend para la plataforma Agro-Solver",
    version="1.0.0"
)

# Configuración CORS
# Permite solicitudes de cualquier origen (útil para desarrollo y producción simple)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. API Endpoints (Prioridad Alta)
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

# 2. Endpoint Raíz (Antes de montar estáticos para asegurar index.html)
@app.get("/")
async def read_root():
    """
    Sirve el archivo frontend/index.html en la raíz.
    """
    return FileResponse('frontend/index.html')

# 3. Archivos Estáticos (Frontend)
# Montamos la carpeta 'frontend' en la raíz para servir CSS, JS y otros assets.
app.mount("/", StaticFiles(directory="frontend"), name="static")
